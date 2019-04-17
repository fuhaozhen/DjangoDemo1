from django.db import models

# Create your models here.


class User(models.Model):
    uname = models.CharField(max_length=20)

    def __str__(self):
        return self.uname


class Good(models.Model):
    gname = models.CharField(max_length=20)
    gprice = models.FloatField()
    guser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.gname

    # 更改后台对象列名显示
    def name(self):
        return self.gname
    name.short_description = "商品名"
