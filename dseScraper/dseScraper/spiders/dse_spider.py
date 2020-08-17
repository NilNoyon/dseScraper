import scrapy

from dseScraper.items import BasicItem
import datetime

#defining connection to mysql server
hostname='127.0.0.1'
username='root'
dbname='dsedb'
password='pass1234'

#importing pymysql
import pymysql.cursors



#establishing connection to mysql server
connection = pymysql.connect(host=hostname,
                             user=username,
                             password=password,
                             db=dbname,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

class dseSpider(scrapy.Spider):
    name = "dse_spider"
    start_urls = [
            'https://www.dse.com.bd/',
    ]


    def parse(self, response):
    	datas = response.css('div.Scroller')
    	# print(datas)
    	for data in datas:
    		brand = data.css('a::text').extract()
    		# print('Hello:  ...',len(brand))
    		brand_list = []
    		amount_list = []
    		status_list = []
    		old_rate_list = []
    		current_rate_list = []
    		counter = 0
    		for i in brand:
    			# print('data: ',i.split('\xa0')[0])
    			counter += 1
    			if (counter % 2) == 0:
    				old_rate_list.append(i.split('\xa0')[0])
    				current_rate_list.append(i.split('\xa0')[4])
    				# print('Odd counter: ',counter)
    			else:
    				brand_list.append(i.split('\xa0')[0])
    				amount_list.append(i.split('\xa0')[1])
    				status_list.append(i.split('\xa0')[2])
    		# print('brand length: ',len(brand_list))
    		# print('amount length: ',len(amount_list))
    		# print('rate length: ',len(old_rate_list))
    		zipped = zip(brand_list, amount_list,old_rate_list,current_rate_list)
    		for brand_list,amount_list, old_rate_list, current_rate_list in zipped:
    			# print('Hello Dear: ',brand_list)
    			if amount_list == '':
    				amount_list = 0
	    		quote_data = BasicItem()
	    		quote_data['brand'] = ''.join(brand_list)
	    		quote_data['amount'] = amount_list
	    		quote_data['status'] = 0
	    		quote_data['old'] = old_rate_list
	    		quote_data['current'] = current_rate_list
	    		quote_data['created_at'] = datetime.datetime.now()
	    		yield quote_data

		    	#uploading to mysql server
		    	with connection.cursor() as cursor:
		    		sql = "INSERT INTO dse(brand, amount, status, old, current, created_at) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (brand_list, amount_list, 0, old_rate_list, current_rate_list, datetime.datetime.now())
		    		cursor.execute(sql)
		    	connection.commit()