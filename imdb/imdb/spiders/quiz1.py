import scrapy


class ScratchQuotes(scrapy.Spider):
    name = 'quiz1'
    start_urls = ['https://www.imdb.com/chart/top/']



    def parse(self, response):
        for movie in response.css('tbody.lister-list .titleColumn '):
            movie_name = movie.css('a::text').get()
            movie_year = movie.css('span::text').get()
            movie_url = movie.css('a::attr(href)').get()

            print(movie_name, movie_year, movie_url)