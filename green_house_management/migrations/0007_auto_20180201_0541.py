# Generated by Django 2.0.1 on 2018-02-01 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_house_management', '0006_auto_20180201_0538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plotsetting',
            old_name='created_by',
            new_name='user',
        ),
    ]