# Generated by Django 2.0.1 on 2018-02-01 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('green_house_management', '0002_auto_20180201_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='row',
            field=models.CharField(max_length=30),
        ),
    ]