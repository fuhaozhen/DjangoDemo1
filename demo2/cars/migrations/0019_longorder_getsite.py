# Generated by Django 2.2 on 2019-05-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0018_auto_20190511_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='longorder',
            name='getsite',
            field=models.CharField(default='金水区', max_length=20),
        ),
    ]
