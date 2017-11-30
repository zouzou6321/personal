from django.contrib import admin
from klines.models import *
# Register your models here.


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
	pass


@admin.register(RealTimeStockData)
class RealTimeStockDataAdmin(admin.ModelAdmin):
	pass
