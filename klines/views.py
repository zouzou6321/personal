from utils.StockData import StockData
from django.http import HttpResponse
from utils.StockNumber import StockNumber
# Create your views here.


def test(request):
	stock_number = StockNumber()
	stock_numbers = stock_number.get_all_stock_number()
	# stock_numbers = stock_number.load_all_stock_number()
	# for stock_number in stock_numbers:
	# 	print(stock_number)
	stock_data = StockData()
	stock_data.load_all_stock_data(stock_numbers)
	return HttpResponse("111")

