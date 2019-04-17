from django.db import models

# Create your models here.


class Good(models.Model):
    gname = models.CharField(max_length=20)
    gprice = models.FloatField()

    def __str__(self):
        return self.gname


class User(models.Model):
    uname = models.CharField(max_length=20)
    ugood = models.ForeignKey("Good", on_delete=models.CASCADE)

    def __str__(self):
        return self.uname
