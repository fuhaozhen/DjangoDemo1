from django.contrib import admin
from .models import *
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "o_uid", "customerName", "customerTel", "o_cid", "typeNo", "creatDate", "returnDate", "otime", "ocost"]
    # 过滤字段
    list_filter = ["id"]
    # 搜索字段
    search_fields = ["o_uid"]


class CarAdmin(admin.ModelAdmin):
    list_display = ["id", "ctype", "typeNo", "picture", "color", "drentprice", "description"]
    # 过滤字段
    list_filter = ["ctype"]
    # 搜索字段
    search_fields = ["typeNo"]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "gender", "idCard", "age", "tel", "addr", "description"]
    # 过滤字段
    list_filter = ["id"]
    # 搜索字段
    search_fields = ["id"]


admin.site.register(Order, OrderAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Customer, CustomerAdmin)
