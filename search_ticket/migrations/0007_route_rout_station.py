# Generated by Django 3.2.9 on 2021-11-23 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search_ticket', '0006_auto_20211123_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='rout_station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='route_station', to='search_ticket.routestation'),
        ),
    ]
