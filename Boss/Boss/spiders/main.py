import scrapy
from scrapy import Request


class ScratchQuotes(scrapy.Spider):
    name = 'boss'
    start_urls = ['https://www.hugoboss.com/men/']

    #
    def parse(self, response):
        css_sel = 'a[href="https://www.hugoboss.com/men-clothing/"] + div .col-xl-offset-1 a::attr(href)'
        print("\n\n\n\n\n\n\n\n")
        for url in response.css(css_sel).getall():
            yield Request(url, callback=self.parseProducts)

    def parseProducts(self, response):
        print('\n\n\n\n\n')
        print(response.url)
        css_sel = '.product-tile-plp__gallery-wrapper a::attr(href)'
        for product_url in response.css(css_sel).getall():
            print(product_url)

