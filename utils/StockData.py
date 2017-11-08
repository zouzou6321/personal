# -*- coding:utf-8 -*-
import requests
from klines.models import RealTimeStockData
import itertools
from celery import task


class StockData:
	per_size = 500

	def __init__(self):
		self.data_url = 'http://hq.sinajs.cn/list='

	def __get_stock_data_one_per(self, quotes_per=[]):
		stock_numbers = []
		for quote in quotes_per:
			stock_numbers.append(quote.stock_number)
		req_para = ','.join(stock_numbers)
		response = requests.get(self.data_url + req_para)
		datas = response.text.split('\n')
		stock_datas = []
		for data in datas[0:-1]:
			stock_data = RealTimeStockData.instance(data.split('\"')[1].split(','))
			stock_datas.append(stock_data)
		return stock_datas

	@task
	def load_all_stock_data(self, quotes=[]):
		stock_data_list = []
		count = 0
		quote_count = len(quotes)
		while count < quote_count:
			stock_data_list = list(itertools.chain(stock_data_list, self.__get_stock_data_one_per(quotes[count: count + self.per_size if count + self.per_size < quote_count else quote_count])))
			count += self.per_size
		RealTimeStockData.objects.bulk_create(stock_data_list)
