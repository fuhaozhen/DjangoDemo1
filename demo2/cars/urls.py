from django.conf.urls import url
from . import views

app_name = 'cars'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^register/$', views.user_register, name='user_register'),
    url(r'^long/$', views.long, name='long'),
    url(r'^short/$', views.short, name='short'),
    url(r'^shangwu/$', views.shangwu, name='shangwu'),
    url(r'^hunqing/$', views.hunqing, name='hunqing'),
    url(r'^daba/$', views.daba, name='daba'),
    url(r'^about/$', views.about, name='about'),
    url(r'^guide/$', views.guide, name='guide'),
    url(r'^order/(\d+)/$', views.order, name='order'),
    url(r'^commit/(\d+)/$', views.commit, name='commit'),
    url(r'^log_out/$', views.log_out, name='log_out'),
    url(r'^userinfo/$', views.userinfo, name='userinfo'),
    url(r'^pay/(\d+)/$', views.pay, name='pay'),
    url(r'^service/$', views.service, name='service'),
    url(r'^online/$', views.online, name='online'),
    url(r'^me/$', views.me, name='me'),
    url(r'^dingdan/$', views.dingdan, name='dingdan'),
    url(r'^xiugai/$', views.xiugai, name='xiugai'),
    url(r'^new/$', views.new, name='new'),
    url(r'^advice/$', views.advice, name='advice'),
    url(r'^success/$', views.success, name='success'),
    url(r'^header/$', views.header, name='header'),
    url(r'^reset/$', views.reset, name='reset'),
    url(r'^changes/$', views.changes, name='changes'),
]