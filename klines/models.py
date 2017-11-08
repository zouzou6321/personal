# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.


class Quote(models.Model):
	stock_number = models.CharField(max_length=20, null=False)
	number = models.CharField(max_length=20, null=False, primary_key=True)
	name = models.CharField(max_length=126, null=False)
	create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	update_time = models.DateTimeField(auto_now=True, null=True, blank=True)

	@classmethod
	def instance(cls, stock_number, number, name):
		instance = Quote()
		instance.stock_number = stock_number
		instance.number = number
		instance.name = name
		return instance


class RealTimeStockData(models.Model):
	name = models.CharField(max_length=20)
	price_today_open = models.DecimalField(max_digits=7, decimal_places=2)
	price_yesterday_close = models.DecimalField(max_digits=7, decimal_places=2)
	price_now = models.DecimalField(max_digits=7, decimal_places=2)
	price_today_max = models.DecimalField(max_digits=7, decimal_places=2)
	price_today_min = models.DecimalField(max_digits=7, decimal_places=2)
	price_buy = models.DecimalField(max_digits=7, decimal_places=2)
	price_sale = models.DecimalField(max_digits=7, decimal_places=2)
	stock_deal_num = models.BigIntegerField()
	stock_deal_money = models.DecimalField(max_digits=15, decimal_places=2)
	stock_buy_one_num = models.BigIntegerField()
	stock_buy_one_price = models.DecimalField(max_digits=7, decimal_places=2)
	stock_buy_two_num = models.BigIntegerField()
	stock_buy_two_price = models.DecimalField(max_digits=7, decimal_places=2)
	stock_buy_three_num = models.BigIntegerField()
	stock_buy_three_price = models.DecimalField(max_digits=7, decimal_places=2)
	stock_buy_four_num = models.BigIntegerField()
	stock_buy_four_price = models.DecimalField(max_digits=7, decimal_places=2)
	stock_buy_five_num = models.BigIntegerField()
	stock_buy_five_price = models.DecimalField(max_digits=7, decimal_places=2)
	stock_sale_one_num = models.BigIntegerField()
	stock_sale_one_price =  models.DecimalField(max_digits=7, decimal_places=2)
	stock_sale_two_num = models.BigIntegerField()
	stock_sale_two_price = models.DecimalField(max_digits=7, decimal_places=2)
	stock_sale_three_num = models.BigIntegerField()
	stock_sale_three_price = models.DecimalField(max_digits=7, decimal_places=2)
	stock_sale_four_num = models.BigIntegerField()
	stock_sale_four_price = models.DecimalField(max_digits=7, decimal_places=2)
	stock_sale_five_num = models.BigIntegerField()
	stock_sale_five_price = models.DecimalField(max_digits=7, decimal_places=2)
	data_date = models.CharField(max_length=10)
	data_time = models.CharField(max_length=8)
	create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	update_time = models.DateTimeField(auto_now=True, null=True, blank=True)

	@classmethod
	def instance(cls, data=[]):
		instance = RealTimeStockData()
		instance.name = data[0]
		instance.price_today_open = data[1]
		instance.price_yesterday_close = data[2]
		instance.price_now = data[3]
		instance.price_today_max = data[4]
		instance.price_today_min = data[5]
		instance.price_buy = data[6]
		instance.price_sale = data[7]
		instance.stock_deal_num = data[8]
		instance.stock_deal_money = data[9]
		instance.stock_buy_one_num = data[10]
		instance.stock_buy_one_price = data[11]
		instance.stock_buy_two_num = data[12]
		instance.stock_buy_two_price = data[13]
		instance.stock_buy_three_num = data[14]
		instance.stock_buy_three_price = data[15]
		instance.stock_buy_four_num = data[16]
		instance.stock_buy_four_price = data[17]
		instance.stock_buy_five_num = data[18]
		instance.stock_buy_five_price = data[19]
		instance.stock_sale_one_num = data[20]
		instance.stock_sale_one_price = data[21]
		instance.stock_sale_two_num = data[22]
		instance.stock_sale_two_price = data[23]
		instance.stock_sale_three_num = data[24]
		instance.stock_sale_three_price = data[25]
		instance.stock_sale_four_num = data[26]
		instance.stock_sale_four_price = data[27]
		instance.stock_sale_five_num = data[28]
		instance.stock_sale_five_price = data[29]
		instance.data_date = data[30]
		instance.data_time = data[31]
		return instance


