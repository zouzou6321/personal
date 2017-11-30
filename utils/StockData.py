# -*- coding:utf-8 -*-
import requests
from klines.models import RealTimeStockData
import itertools
from celery import task
from utils.StockNumber import StockNumber


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

	def load_all_stock_data(self, quotes=[]):
		count = 0
		quote_count = len(quotes)
		while count < quote_count:
			RealTimeStockData.objects.bulk_create(self.__get_stock_data_one_per(
				quotes[count: count + self.per_size if count + self.per_size < quote_count else quote_count]))
			count += self.per_size

@task
def load_func():
	stock_number = StockNumber()
	stock_numbers = stock_number.get_all_stock_number()
	# stock_numbers = stock_number.load_all_stock_number()
	# for stock_number in stock_numbers:
	# 	print(stock_number)
	stock_data = StockData()
	stock_data.load_all_stock_data(stock_numbers)