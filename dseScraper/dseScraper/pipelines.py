# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sys
from dseScraper.items import BasicItem
import pymysql

class DsescraperPipeline:
	def __init__(self):
		# 1. Establish a connection to the database
        self.connect = pymysql.connect(
        # Localhost is connected to a local database
            host='127.0.0.1',
            port=3306,
            user='root',
            password='',
            database='dsedb',
        )
        # 2. Create a cursor cursor, it is used to operate the table.
        self.cursor = self.connect.cursor()

	def process_item(self, item, spider):
		data = BasicItem(**item)
		# 3. Item data into the database, the default is synchronous writes.
        insert_sql = "INSERT INTO dse(brand, amount, status, old, current, created_at) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (item['brand'], item['amount'], item['status'], item['old'], item['current'], item['created_at'])
        self.cursor.execute(insert_sql)
        print('After Insert into database')
        # 4. commit operation
        self.connect.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
        print('After closing the connection')