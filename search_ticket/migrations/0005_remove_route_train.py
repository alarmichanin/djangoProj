# Generated by Django 3.2.9 on 2021-11-23 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_ticket', '0004_route_rout_train'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='train',
        ),
    ]
