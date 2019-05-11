from django.contrib import admin
from .models import *
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "o_uid", "customerName", "customerTel", "o_cid", "typeNo", "creatDate", "returnDate", "otime", "ocost", "is_return"]
    # 过滤字段
    list_filter = ["id"]
    # 搜索字段
    search_fields = ["o_uid"]


class CarAdmin(admin.ModelAdmin):
    list_display = ["id", "ctype", "carnum", "typeNo", "picture", "color", "drentprice", "description"]
    # 过滤字段
    list_filter = ["ctype"]
    # 搜索字段
    search_fields = ["typeNo"]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "picture",  "gender", "idCard", "age", "tel", "addr", "description"]
    # 过滤字段
    list_filter = ["id"]
    # 搜索字段
    search_fields = ["id"]


class AdviceAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "gender", "email", "phone", "title", "content"]
    list_filter = ["name"]
    search_fields = ["name"]


class HotAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "pic", "index"]
    list_filter = ["name"]
    search_fields = ["name"]


admin.site.register(Order, OrderAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Advice, AdviceAdmin)
admin.site.register(Hotpic, HotAdmin)
