# -*- coding:utf-8 -*-
import timeit
import requests
import itertools
from klines.models import Quote
from utils.MyThread import MyThread
from celery import task


class StockNumber:
	all_quotes_url = 'http://money.finance.sina.com.cn/d/api/openapi_proxy.php'
	#sh000001 = {'Symbol': '000001.SS', 'Name': '上证指数'}
	#sz399001 = {'Symbol': '399001.SZ', 'Name': '深证成指'}
	#sh000300 = {'Symbol': '000300.SS', 'Name': '沪深300'}

	def __init__(self):
		self.page_size = 500

	def __load_stock_one_per(self, page, page_size):
		para_val = '[["hq","hs_a","",0,' + str(page) + ',' + str(page_size) + ']]'
		r_params = {'__s': para_val}
		r = requests.get(self.all_quotes_url, params=r_params)
		data_info = {
			'count': int(r.json()[0]['count']),
			'quotes': []
		}
		for item in r.json()[0]['items']:
			quote = Quote.instance(item[0], item[1], item[2])
			data_info['quotes'].append(quote)

		return data_info

	def load_all_stock_number(self):
		print("load_all_stock_number start..." + "\n")

		start = timeit.default_timer()

		all_quotes = []

		try:
			stock_count = self.__load_stock_one_per(1, 1)['count']
			count = 0
			g_func_list = []
			while count < stock_count:
				count += self.page_size
				g_func_list.append({"func": self.__load_stock_one_per, "args": (count / self.page_size, self.page_size)})
			my_thread = MyThread()
			my_thread.set_thread_func_list(g_func_list)
			my_thread.start()
			for data_info in my_thread.ret_value():
				all_quotes = list(itertools.chain(all_quotes, data_info['quotes']))
			Quote.objects.all().delete()
			Quote.objects.bulk_create(all_quotes)
		except Exception as e:
			print("Error: Failed to load all stock number..." + "\n")
			print(e)

		print("load_all_stock_number end... time cost: " + str(round(timeit.default_timer() - start)) + "s" + "\n")
		return all_quotes

	def get_all_stock_number(self):
		return list(Quote.objects.all())


@task
def load_all_stock_number():
	stock_number = StockNumber()
	stock_number.load_all_stock_number()
