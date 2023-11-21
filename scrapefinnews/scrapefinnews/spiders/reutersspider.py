import scrapy

class ReutersspiderSpider(scrapy.Spider):
    name = "reutersspider"
    allowed_domains = ["www.reuters.com"]
    start_urls = ["https://www.reuters.com/"]


    def parse(self, response):
        pass
