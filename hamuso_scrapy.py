class HamusoSpider(scrapy.Spider):
    name = 'hamuso'
    start_urls = ['https://migraine.com/living-migraine/migraine-whispers-poison-ear/#comments_anchor']                                                             ar/#comments_anchor']
    def parse(self, response):
        for com in response.css('Span.comment-body'):
            text = {'comment': com.css('.comment-text').extract()}
            yield text
        for com in response.css('section#comments'):
            user = {'User': com.css('a.comment-user').extract()}
            yield user
        for com in response.css('Span.comment-meta'):
            date = {'date/time': com.css('.comment-meta').extract()}
            yield date
