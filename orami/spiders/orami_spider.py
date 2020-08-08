# scrapy shell "https://www.orami.co.id/ap/takoyakids"
# buat mencari pattern xpath atau css
# running -> scrapy crawl orami
# cheats https://devhints.io/xpath

""" 
--- Export as CSV Feed ---
FEED_FORMAT = "csv"
FEED_URI = "result.csv"
--- save in settings.py ---
"""
import scrapy

class OramiSpider(scrapy.Spider):
    name = "orami"

    def start_requests(self):
        urls = [
            'https://www.orami.co.id/ap/takoyakids',
            'https://www.orami.co.id/c/peralatan-bayi',
            'https://www.orami.co.id/c/fashion-dan-aksesoris'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # results = response.xpath("//button[contains(@onclick, 'pushOnclick')]/@onclick").extract()
        # words = [w.replace('pushOnclick(', '').replace(');', '') for w in results]
        # for w in results:
        #     item = w.replace('pushOnclick(', '').replace(');', '').replace("'", '').split(',')
        #     scraped_info = {
        #             'ID' : item[0],
        #             'NAMA PRODUK' : item[1],
        #             'URL' : item[4],
        #             'HARGA' : item[2],
        #             }
        #     yield scraped_info

        price = response.xpath("//div[contains(@class, 'widget-price mb-8')]//p/text()").extract()
        name_product = response.xpath("//div[contains(@class, 'prod-name mb-8')]//a/text()").extract()

        for item in zip(price,name_product):
            scraped_info = {
                'price' : item[0],
                'name_product' : item[1].lstrip().rstrip(),
                }  
            yield scraped_info          
