# Generated by Django 2.2 on 2019-05-11 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0016_longcar_longorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='longorder',
            name='cartype',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cars.LongCar'),
        ),
    ]
