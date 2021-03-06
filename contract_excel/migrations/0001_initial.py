# Generated by Django 2.2.2 on 2019-08-02 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract_Info',
            fields=[
                ('contract_num', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('supplier', models.CharField(max_length=20)),
                ('agent', models.CharField(max_length=10)),
                ('goods', models.CharField(max_length=40)),
                ('purchase', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('currency', models.CharField(max_length=5)),
                ('port', models.CharField(max_length=20)),
                ('delivery_date', models.DateField()),
            ],
            options={
                'verbose_name': '合同信息',
                'verbose_name_plural': '合同信息',
                'db_table': 'contract_info',
            },
        ),
    ]
