# Generated by Django 2.2 on 2019-05-01 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_auto_20190429_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='creatDate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='returnDate',
            field=models.DateTimeField(),
        ),
    ]
