"""
通过少量的代码实现强大的后台管理
需要将特定的数据模型注册 才能在后台管理
python manage.py createsuperuser 创建超级管理员
"""
from django.contrib import admin
from .models import BookInfo, HeroInfo
admin.site.register(BookInfo)
admin.site.register(HeroInfo)

# Register your models here.
