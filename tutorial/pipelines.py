# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import json
import codecs

class TutorialPipeline(object):
	def __init__(self):
		self._file = codecs.open("out.json", "w", encoding="utf-8")

    	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False)+"\n"
		self._file.write(line)
        	return item

	def spider_closed(self, spider):
		self._file.close()
