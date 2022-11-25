import scrapy


class ScratchQuotes(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']


    def parse(self, response):
        for div in response.css('.quote'):
            yield {
                'quote': div.css('.text::text').get(),
                'author': div.css('.author::text').get()
            }
