# -*- coding: utf-8 -*-

BOT_NAME = 'imdb_scraper'

SPIDER_MODULES = ['imdb_scraper.spiders']
NEWSPIDER_MODULE = 'imdb_scraper.spiders'

# Saving the output in json format
FEED_URI = 'data/%(name)s.json'
FEED_FORMAT = 'json'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DEFAULT_REQUEST_HEADERS = {
    'Referer': 'https://www.imdb.com',
    'User-Agent': 'PostmanRuntime/7.32.3',
    'accept-encoding': 'gzip, deflate, br, zstd',
    # setup lang here. /!\ may change parse patterns
    'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache'
}
