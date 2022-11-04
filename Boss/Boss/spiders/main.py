import scrapy


class ScratchQuotes(scrapy.Spider):
    name = 'boss'
    start_urls = ['https://www.imdb.com/chart/top/']


    def parse(self, response):
        pass