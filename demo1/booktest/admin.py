"""
通过少量的代码实现强大的后台管理
需要将特定的数据模型注册 才能在后台管理
python manage.py createsuperuser 创建超级管理员
"""
from django.contrib import admin
from .models import BookInfo, HeroInfo


class HeroInfoInline(admin.StackedInline):
    """
    实现关联注册，即创建书名的时候可以创建角色名
    """
    model = HeroInfo
    # 关联个数
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    """
    通过定义ModelAdmin的子类，来定义模型在Admin的显示方式
    """
    # 显示字段，可以点击列头进行排序
    list_display = ["id", "name", "bpub_date"]
    # 过滤字段，过滤框会出现在右侧
    list_filter = ["btitle"]
    # 搜索字段，搜索框会出现在上边
    search_fields = ["btitle"]
    # 分页，分页框会出现在下边
    list_per_page = 2

    # 关联注册
    inlines = [HeroInfoInline]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "hname", "hgender", "hcontent", "hbook"]
    list_filter = ["hgender"]
    search_fields = ["hname"]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)

# Register your models here.
