# coding:utf-8

from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

app_name = 'traderlife'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index,name='index'),
    url(r'login_action$', views.login_action),
    # url(r'^event_manage', views.event_manage),
    url(r'^accounts/login/$', views.index),
    url(r'^gamepage', views.gamepage),
    url(r'^submitOrder', views.submitOrder),  # 获取订单的ajax
    url(r'^updateWareHouse', views.updateWarehouse),  # 更新warehouse ajax
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/favicon.ico')),  # 设置favicon
    url(r'^gameover', views.gameover),
    url(r'^nextTurn', views.nextTurn),
    url(r'newGame$', views.newGame),
    url(r'^register', views.register),
    url(r'^getAccountInfo', views.getAccountInfo),
    url(r'logout', views.logout_action),
    url(r'myphone/homepage', views.myphone_homepage),
    url(r'myphone/message', views.myphone_message),
    url(r'myphone/news', views.myphone_news),
    url(r'myphone/about', views.myphone_about),
]