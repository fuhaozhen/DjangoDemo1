from django.db import models
# 导入django框架内置的用户模块
from django.contrib.auth.models import User
# Create your models here.

# 富文本编辑器
from tinymce.models import HTMLField


class Customer(models.Model):
    """
    定义用户扩展类型，和系统内置用户一对一关联
    """
    # 客户头像
    picture = models.ImageField(upload_to="picture")
    # 客户性别
    gender = models.CharField(max_length=20)
    # 客户身份证号
    idCard = models.CharField(max_length=50)
    # 客户年龄
    age = models.IntegerField(default=20)
    # 客户电话
    tel = models.CharField(max_length=50)
    # 客户地址
    addr = models.CharField(max_length=50)
    # 备注信息
    description = models.CharField(max_length=50)

    # 关联
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Car(models.Model):
    """车辆信息"""
    # 车辆种类
    ctype = models.CharField(default="轿车", max_length=20)
    # 车辆型号
    typeNo = models.CharField(max_length=20)
    # 车辆库存
    carnum = models.IntegerField(default=100)
    # 车辆图片
    picture = models.FileField(null=True, upload_to="./static/media/")
    # 颜色
    color = models.CharField(max_length=20)
    # 日出租价格
    drentprice = models.FloatField()
    # 描述
    description = models.CharField(max_length=50, default="//5座 自动/1.5L")

    def __str__(self):
        return self.ctype


class Order(models.Model):
    """订单信息"""
    # 客户ID
    o_uid = models.ForeignKey(User, on_delete=models.CASCADE)
    # 客户姓名
    customerName = models.CharField(max_length=20)
    # 客户电话
    customerTel = models.CharField(max_length=50)
    # 车辆ID
    o_cid = models.ForeignKey(Car, on_delete=models.CASCADE)
    # 车辆号
    typeNo = models.CharField(max_length=20)
    # 取车时间
    creatDate = models.DateTimeField(auto_now_add=False)
    # 还车时间
    returnDate = models.DateTimeField(auto_now_add=False)
    # 租赁时长
    otime = models.IntegerField(default=0)
    # 总费用
    ocost = models.FloatField()

    choice = (('T', '已还车'), ('F', '租赁中'),)
    # 是否已还车
    is_return = models.CharField(choices=choice, max_length=20, default='T')




class Advice(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    content = HTMLField()


class Hotpic(models.Model):
    name = models.CharField(max_length=20)
    pic = models.ImageField(upload_to='hotpic')
    index = models.IntegerField()

