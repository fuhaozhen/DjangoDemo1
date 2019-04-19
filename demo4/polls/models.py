from django.db import models

# Create your models here.


class Question(models.Model):
    qtext = models.CharField(max_length=50)

    def __str__(self):
        return self.qtext


class Choice(models.Model):
    cchoice = models.CharField(max_length=20)
    cvote = models.IntegerField(default=0)
    cquestion = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.cchoice
