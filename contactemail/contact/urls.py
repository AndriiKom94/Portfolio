from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('scrapy/', views.scrapy, name="scrapy"),
    path('ecommerce/', views.ecommerce, name="ecommerce"),
    path('excel/', views.excel, name="excel"),
]