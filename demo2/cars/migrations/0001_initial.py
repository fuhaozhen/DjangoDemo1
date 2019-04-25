# Generated by Django 2.2 on 2019-04-24 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctype', models.CharField(default='轿车', max_length=20)),
                ('typeNo', models.CharField(max_length=20)),
                ('picture', models.FileField(null=True, upload_to='./static/media/')),
                ('color', models.CharField(max_length=20)),
                ('drentprice', models.FloatField()),
                ('description', models.CharField(default='//5座 自动/1.5L', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=20)),
                ('customerTel', models.CharField(max_length=50)),
                ('typeNo', models.CharField(max_length=20)),
                ('creatDate', models.DateTimeField(auto_now_add=True)),
                ('returnDate', models.DateTimeField(auto_now_add=True)),
                ('otime', models.IntegerField(default=0)),
                ('ocost', models.FloatField()),
                ('o_cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Car')),
                ('o_uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=20)),
                ('idCard', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=20)),
                ('tel', models.CharField(max_length=50)),
                ('addr', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]