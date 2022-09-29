#!/usr/bin/env python

import argparse
import feedparser
import yaml


struct = {"title": [], "link": [], "summary": []}
parser = argparse.ArgumentParser(description="A simple rss feed consumer")
parser.add_argument('url', type=str, nargs='?', help='An optional rss feed url')
parser.add_argument('-s', '--source', type=str, help='An optional source argument - ignored if a url is provided; '
                                               'corresponds to one of the keys from '
                                               'the configuration file conf_file.yaml')
parser.add_argument('-f', '--file', type=str, help='An optional file argument; if provided the result will be written '
                                                   'to the file else output is written to stdout')


def consume_feed(url, file=None):
    def write(args: str):
        if file:
            with open(file, 'a') as f:
                f.write(args + '\n')
            pass
        else:
            return print(args)

    feed = feedparser.parse(url)
    if feed:
        for item in feed["items"]:
            for key in struct.keys():
                try:
                    write(item[key])
                except KeyError:
                    pass
            write("_____________________________________________")
    return True


if __name__ == "__main__":
    args = parser.parse_args()
    file = args.file
    if args.url:
        consume_feed(args.url)
    else:
        with open("./rss.yaml") as conf:
            sources = yaml.load(conf, Loader=yaml.FullLoader)
            if args.source:
                try:
                    urls = sources[args.source]
                    for url in urls:
                        consume_feed(url, file=file)
                except KeyError:
                    print(f"Source '{args.source}' was not found in the configuration file")
            else:
                for journal, urls in sources.items():
                    print(journal)
                    for url in urls:
                        consume_feed(url, file=file)
