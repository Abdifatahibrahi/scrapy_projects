import scrapy


class ScratchQuotes(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/']


    def parse(self, response):
        for movie in response.css('tbody.lister-list .titleColumn a'):
            name = movie.css('::text').get()
            movie_url = movie.css('::attr(href)').get()
            print(name, movie_url)
