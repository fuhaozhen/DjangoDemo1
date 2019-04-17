from django.contrib import admin
from .models import *
# Register your models here.


class GoodAdmin(admin.ModelAdmin):
    """自定义管理界面"""
    # 显示字段
    list_display = ["id", "gname", "gprice"]
    # 过滤字段
    list_filter = ["gname"]
    # 搜索字段
    search_fields = ["gname"]


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "uname", "ugood"]


admin.site.register(Good, GoodAdmin)
admin.site.register(User, UserAdmin)
