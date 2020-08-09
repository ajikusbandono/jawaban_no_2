# jawaban_no_2

OS : Windows 10

Env : Python 2.7

Framework : https://scrapy.org

Target crawling : www.orami.co.id

Pattern : Xpath

Result : Price, Product and link

Validation : pivot in excel for crawling validation 

File type : csv

Explode target : 

			<div class="widget-price mb-8">
				<p class="price-range">Mulai Rp 89.000</p>
			</div>
      
			<div class="prod-name mb-8">
				<a itemprop="url" href="https://www.orami.co.id/takoyakids-minori-sets-steel-blue.html" onclick="pushOnclick('240813', 'Takoyakids Minori Sets Steel Blue', 89000, 'Takoyakids', 'https://www.orami.co.id/takoyakids-minori-sets-steel-blue.html', 147, '','Baby \x26 Kids');">
				Takoyakids Minori Sets Steel Blue                </a>
			</div>      
      
How to use : just add url category into array list on orami_spider.py under orami/spider path or put single root url

How to run : 
	     
	     1. goto directory and put this line -> scrapy crawl orami
             
	     2. you can file output csv automatically on directory
	  
