# Generated by Django 3.2.9 on 2021-11-23 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_ticket', '0002_auto_20211123_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='railcar',
            name='amount_of_seats',
            field=models.PositiveBigIntegerField(blank=True, default=40, null=True),
        ),
    ]
