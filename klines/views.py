# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from klines.models import RealTimeStockData
import datetime
# Create your views here.


'''
获取涨跌幅最大的20支
'''
def swing_top(request):
	today = datetime.datetime.now()
	if today.hour < 13:
		today -= datetime.timedelta(1)
	increase = RealTimeStockData.objects.raw(
		"select max(id) as id from klines_realtimestockdata where create_time>'%s-%s-%s 00:00:00' and price_today_open > 0 GROUP BY name order by (max(price_now) - max(price_today_open)) / max(price_today_open) desc limit 10" % (today.year, today.month, today.day))
	res = ''
	for a in increase:
		res += a.to_json()
	return render(request, "index.html", {"res": res})


def down_top(request):
	today = datetime.datetime.now()
	if today.hour < 13:
		today -= datetime.timedelta(1)
	decrease = RealTimeStockData.objects.raw(
		"select max(id) as id from klines_realtimestockdata where create_time>'%s-%s-%s 00:00:00' and price_today_open > 0 GROUP BY name order by (max(price_now) - max(price_today_open)) / max(price_today_open) asc limit 10" % (today.year, today.month, today.day))

	res = ''
	for a in decrease:
		res += a.to_json()
	return HttpResponse(res)


'''根据信息做出决定'''
def decision(request):
	pass


def summary(request):
	pass
