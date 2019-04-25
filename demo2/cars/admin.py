from django.contrib import admin
from .models import *
# Register your models here.


# class UserAdmin(admin.ModelAdmin):
#     list_display = ["id", "name", "pwd", "gender", "tel", "role"]
#

class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "o_uid", "customerName", "customerTel", "o_cid", "typeNo", "creatDate", "returnDate", "otime", "ocost"]


class CarAdmin(admin.ModelAdmin):
    list_display = ["id", "ctype", "typeNo", "picture", "color", "drentprice", "description"]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "gender", "idCard", "age", "tel", "addr", "description"]


# admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Customer, CustomerAdmin)
