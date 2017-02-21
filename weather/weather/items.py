# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
	title = scrapy.Field()
    time = scrapy.Field()
    temp = scrapy.Field()
    describe = scrapy.Field()
    rain = scrapy.Field()
    # pass
