# Generated by Django 2.2.2 on 2020-03-11 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract_excel', '0014_auto_20200311_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harmonized_system_customer',
            name='goods_en_name',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
