# Generated by Django 2.2.2 on 2020-03-11 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract_excel', '0012_auto_20200311_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harmonized_system_customer',
            name='unit_price',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
    ]