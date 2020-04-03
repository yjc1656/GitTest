# Generated by Django 2.2.2 on 2020-03-10 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract_excel', '0006_auto_20200310_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harmonized_system_customer',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='harmonized_system_customer',
            name='unit_price',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]