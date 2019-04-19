from django.conf.urls import url
from . import views

# 给应用添加app_name
app_name = "booktest"
urlpatterns = [
    # url("index/", views.index),
    # 第三个参数为命名空间
    url(r"^$", views.index, name="index"),
    url(r"^list/$", views.list, name="list"),
    url(r"^detail/(\d+)/", views.detail, name="detail"),
    url(r"^add/$", views.add, name="add"),
    url(r"^delete/(\d+)/$", views.delete, name="delete"),
    url(r"^addhero/(\d+)/$", views.addhero, name="addhero"),
    url(r"^addherohandler/$", views.addherohandler, name="addherohandler"),
    url(r"^deletehero/(\d+)/$", views.deletehero, name="deletehero"),
]

