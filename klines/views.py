# -*- coding:utf-8 -*-
from django.http import HttpResponse
from klines.models import RealTimeStockData
import datetime
# Create your views here.


def swing_top(request):
	today = datetime.datetime.now()
	if today.hour < 13:
		today -= datetime.timedelta(1)
	increase = RealTimeStockData.objects.raw(
		"select * from klines_realtimestockdata where create_time>'" + str(today) + " 00:00:00' and price_today_open > 0 order by (price_today_open - price_now) / price_today_open desc limit 10")
	decrease = RealTimeStockData.objects.raw(
		"select * from klines_realtimestockdata where create_time>'" + str(today) + " 00:00:00' and price_today_open > 0 order by (price_today_open - price_now) / price_today_open asc limit 10")

	res = []
	for a in increase:
		print(a.to_json())
		res.append(a.to_json())
	for a in decrease:
		print(a.to_json())
		res.append(a.to_json())
	return HttpResponse(res)
