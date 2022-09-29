# RSS-FEED

A simple rss feed consumer.
Provide URLs from the command line or in the rss.yaml file and get the news on your terminal.

## Dependencies

	feedparser==6.0.10
	pyaml==21.10.1

## Usage: 

	rss_feed.py [-h] [-s SOURCE] [-f FILE] [url]

A simple rss feed consumer

positional arguments:
  
	url                   An optional rss feed url

options:

  	-h, --help            		show this help message and exit
  	
	-s SOURCE, --source SOURCE	An optional source argument - ignored if a url is provided; corresponds to one of the keys from the configuration file rss.yaml

	-f FILE, --file FILE  		An optional file argument; if provided the result will be written to the file else output is written to stdout

