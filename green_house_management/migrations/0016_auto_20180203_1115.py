# Generated by Django 2.0.1 on 2018-02-03 11:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('green_house_management', '0015_auto_20180203_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='device',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alert',
            name='plot',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sensorinformation',
            name='water_content',
            field=models.PositiveIntegerField(),
        ),
    ]
