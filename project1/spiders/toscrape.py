import scrapy


class ToscrapeSpider(scrapy.Spider):
    name = 'toscrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        products = response.xpath('.//article[@class="product_pod"]')
        for product in products:
            img_url = product.xpath('.//img/@src').get()
            title = product.xpath('.//h3/a/text()').get()
            price = product.xpath('.//p[@class="price_color"]/text()').get().strip()

            yield {
            'img_link':img_url,
            'title':title,
            'price':price }

        next_page = response.xpath('.//li[@class="next"]/a/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)