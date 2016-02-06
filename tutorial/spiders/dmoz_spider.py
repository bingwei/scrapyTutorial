from scrapy import Spider
from tutorial.items import DmozItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class DmozSpider(Spider):
	name = "dmoz"
	allowed_domains = ["dmoz.org"]
	start_urls = ["http://www.dmoz.org/Computers/Programming/Languages/Python/Books/", 
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"  
    ]

	def parse(self, response):
		for site in response.xpath("//ul[@class='directory-url']/li"):
			item = DmozItem()
			item['title'] = site.xpath('./a/text()').extract()		
			item['link'] = site.xpath('./a/@href').extract()		
			item['desc'] = [x.strip() for x in site.xpath('./text()').extract()]
			yield item
