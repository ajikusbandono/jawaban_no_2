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
            'https://www.orami.co.id/',
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.getlink)

    def getlink(self, response):
        links = response.xpath("//div[contains(@class, 'oss-u-1-8 pl-8 pr-8')]/div/a/@href").extract()
        
        for link in links:
            try:
                yield scrapy.Request(url=link, callback=self.parse)
            except:
                _link =  'https://www.orami.co.id' + link
                yield scrapy.Request(url=_link, callback=self.parse)
     
    def parse(self, response):
        
        _res = response.url
        _price = response.xpath("//div[contains(@class, 'widget-price mb-8')]//p/text()").extract()
        _name_product = response.xpath("//div[contains(@class, 'prod-name mb-8')]//a/text()").extract()

        for _item in zip(_price,_name_product):
            scraped_info = {
                'price' : _item[0],
                'name_product' : _item[1].lstrip().rstrip(),
                'link' : _res
                }  
            yield scraped_info
             