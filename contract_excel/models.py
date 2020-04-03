from django.db import models

# Create your models here.


class Contract_Info(models.Model):
    contract_num = models.CharField(max_length=40,primary_key=True)
    supplier = models.CharField(max_length=20)
    agent = models.CharField(max_length=10)
    goods = models.CharField(max_length=40)
    purchase = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=5)
    port = models.CharField(max_length=20)
    delivery_date = models.DateField()

    class Meta:
        db_table = 'contract_info'
        verbose_name = '合同信息'
        verbose_name_plural = '合同信息'


class Harmonized_System(models.Model):
    custom = models.CharField(max_length=20, blank=True)  # 厂家
    goods_en_name = models.CharField(max_length=150, blank=True)    # 英文名称
    goods_zh_name = models.CharField(max_length=150, blank=True)    # 中文名称
    product_code = models.CharField(max_length=40, blank=True)  # 产品编码
    goods_code = models.CharField(max_length=40, blank=True)    # 长裕编码
    property = models.CharField(max_length=100, blank=True)  # 产品性能
    hs_code = models.CharField(max_length=20, blank=True)   # HS编码
    hs_name = models.TextField(blank=True)  # 申报要素
    note = models.TextField(blank=True)  # 备注

    class Meta:
        db_table = 'hs_info'
        verbose_name = 'HS编码信息'
        verbose_name_plural = 'HS编码信息'


class Harmonized_System_Customer(models.Model):
    custom = models.CharField(max_length=20, blank=True)  # 厂家
    goods_code = models.CharField(max_length=40, blank=True)  # 长裕编码
    goods_zh_name = models.CharField(max_length=150, blank=True)  # 中文名称
    part_num = models.CharField(max_length=40, blank=True)  # 零件号
    goods_en_name = models.CharField(max_length=500, blank=True)  # 英文名称
    subull_crapidiary = models.CharField(max_length=40, blank=True)  # 隶属机构
    unit_price = models.DecimalField(max_digits=15, decimal_places=3, blank=True)  # 单价 3位整数 三位小数
    quantity = models.IntegerField()  # 数量
    hs_code = models.CharField(max_length=20, blank=True)   # HS编码
    hs_name = models.TextField(blank=True)  # 申报要素s
    contract_num = models.CharField(max_length=30, blank=True)  # 合同号
    purchase_year = models.CharField(max_length=10, blank=True)  # 采购时间

    class Meta:
        db_table = 'hs_info_new'
        verbose_name = 'HS客户编码信息'
        verbose_name_plural = 'HS客户编码信息'
