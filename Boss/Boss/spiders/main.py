import scrapy


class ScratchQuotes(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']


    def parse(self, response):
        for div in response.css('.quote'):
            quotes = div.css('.text::text').get()
            yield {
                'quote': quotes.replace('“', '').replace('”', ''),
                'author': div.css('.author::text').get()
            }

        next_url = response.css('li.next a::attr(href)').get()

        if next_url:
            yield response.follow(next_url, callback=self.parse)

