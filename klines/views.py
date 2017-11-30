# -*- coding:utf-8 -*-
from django.http import HttpResponse
from klines.models import RealTimeStockData
import itertools
import datetime
from utils.StockData import load_func
# Create your views here.


def swing_top(request):
	load_func()
	today = datetime.date.today()
	increase = RealTimeStockData.objects.raw(
		"select * from klines_realtimestockdata where create_time>'" + str(today) + " 15:00:00' and price_today_open > 0 order by (price_today_open - price_now) / price_today_open desc limit 10")
	decrease = RealTimeStockData.objects.raw(
		"select * from klines_realtimestockdata where create_time>'" + str(today) + " 15:00:00' and price_today_open > 0 order by (price_today_open - price_now) / price_today_open asc limit 10")

	res = []
	for a in increase:
		print a
		res.append(a)
	for a in decrease:
		print a
		res.append(a)
	return HttpResponse('1111')
