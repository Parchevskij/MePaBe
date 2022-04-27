import scrapy
import scraper_helper as sh
import time

class FirstSpider(scrapy.Spider):
    name = 'rbc.ru'
    start_urls = ['https://www.rbc.ru/story/5422bb83cbb20f63f25fb481']
    #start_urls = ['https://www.rbc.ru/politics/?utm_source=topline']

    def parse(self, response, **kwargs):
        for link in response.css('div.item__wrap.l-col-center a::attr(href)'):
            yield response.follow(link, callback=self.text)

    def text(self, response):
        yield {
            'text': ''.join(response.css('div.article__text.article__text_free p::text').getall()),
            #'text': ''.join([sh.cleanup(x) for x in response.css('div.article__text.article__text_free p::text').getall()]),
            'date': response.css('span.article__header__date::attr(content)').get()
        }



