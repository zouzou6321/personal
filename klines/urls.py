from django.conf.urls import url
from klines.views import *
urlpatterns = [
    url(r'^', swing_top),
]