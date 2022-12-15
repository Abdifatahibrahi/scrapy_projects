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
            break

    def parseProducts(self, response):
        print('\n\n\n\n\n')
        print(response.url)
        css_sel = '.product-tile-plp__gallery-wrapper a::attr(href)'
        for product_url in response.css(css_sel).getall():
            yield response.follow(product_url, callback=self.parseProduct)
            break

    def parseProduct(self, response):
        print('\n\n\n\n\n')
        print(response.url)
        product_title = response.css('h1.pdp-stage__header-title::text').get().strip()
        product_price = response.css('.pricing__header .pricing__main-price::text').get().strip()
        care_inst = response.css('.care-info .care-info__text::text').getall()
        care_inst = ' , '.join(care_inst)
        model = response.css('#product-container-sizefit-panel::text').get().strip()

        print(product_title, product_price, care_inst, model)




