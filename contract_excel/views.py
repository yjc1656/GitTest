from django.shortcuts import render, redirect
from django.db import transaction
from contract_excel.models import Harmonized_System, Harmonized_System_Customer
import xlrd, decimal
from contract_app.views import login_check


# Create your views here.


@login_check
def hs_info(request):
    if request.method == 'POST':
        hs_file = request.FILES['hs_code']
        hs_code = xlrd.open_workbook(filename=None, file_contents=hs_file.read())  # 关键点在于这里
        hs_excel = hs_code.sheets()[0]
        # print(hs_excel)
        rows = hs_excel.nrows
        if rows > 0:
            hs_codes = Harmonized_System.objects.all()
            hs_codes.delete()
        try:
            with transaction.atomic():
                for i in range(2, rows):
                    rowValues = hs_excel.row_values(i)  # 一行的数据
                    hs_code = Harmonized_System()
                    hs_code.custom = rowValues[0]
                    hs_code.goods_en_name = rowValues[1]
                    hs_code.goods_zh_name = rowValues[2]
                    hs_code.product_code = rowValues[3]
                    hs_code.goods_code = rowValues[4]
                    hs_code.property = rowValues[5]
                    hs_code.hs_code = rowValues[6]
                    hs_code.hs_name = rowValues[7]
                    hs_code.note = rowValues[8]
                    hs_code.save()
                    hs_code.clean_fields()
        except Exception as e:
            return render(request, 'contract_excel/hs_info_import.html', {"message": '出现错误....'})
            # return JsonResponse({'msg': '出现错误....'})
        return redirect('/hs_code')
    else:
        return render(request, 'contract_excel/contract_info.html')


@login_check
def hs_code(request):
    if request.method == 'POST':
        customer = request.POST.get('custom')
        en_name = request.POST.get('en_name')
        zh_name = request.POST.get('zh_name')
        product = request.POST.get('product')
        cybm = request.POST.get('cybm')
        code = request.POST.get('hs_code')
        hs_codes = Harmonized_System.objects.filter(custom__icontains=customer,
                                                    goods_en_name__contains=en_name,
                                                    goods_zh_name__contains=zh_name,
                                                    product_code__contains=product,
                                                    goods_code__contains=cybm,
                                                    hs_code__contains=code
                                                    )
        print(hs_codes)
        return render(request, 'contract_excel/hs.html', {'hs_codes': hs_codes})
    else:
        return render(request, 'contract_excel/hs.html')


@login_check
def hs_info_new(request):
    if request.method == 'POST':
        hs_file_new = request.FILES['hs_code_new']
        hs_code_new = xlrd.open_workbook(filename=None, file_contents=hs_file_new.read())  # 关键点在于这里
        hs_excel_new = hs_code_new.sheets()[0]
        # print(hs_excel)
        rows = hs_excel_new.nrows
        if rows > 0:
            hs_codes_new = Harmonized_System_Customer.objects.all()
            # hs_codes_new.delete()
        try:
            with transaction.atomic():
                for i in range(1, rows):
                    rowValues = hs_excel_new.row_values(i)  # 一行的数据
                    # 创建对象
                    hs_code_new = Harmonized_System_Customer()
                    hs_code_new.custom = rowValues[0]  # 厂家
                    hs_code_new.goods_code = rowValues[1]  # 长裕编码
                    hs_code_new.goods_zh_name = rowValues[2]  # 中文名称
                    hs_code_new.part_num = rowValues[3]  # 零件号
                    hs_code_new.goods_en_name = rowValues[4]  # 英文名称
                    hs_code_new.subull_crapidiary = rowValues[5]  # 隶属机构
                    if type(rowValues[6]) == float:
                        hs_code_new.unit_price = decimal.Decimal(rowValues[6]).quantize(decimal.Decimal('0.000'))  # 单价
                    else:
                        hs_code_new.unit_price = 0

                    if type(rowValues[6]) == float:
                        hs_code_new.quantity = rowValues[7]  # 数量
                    else:
                        hs_code_new.quantity = 0
                    hs_code_new.hs_code = rowValues[8]  # HS编码
                    hs_code_new.hs_name = rowValues[9]  # 申报要素
                    hs_code_new.contract_num = rowValues[10]  # 合同号
                    hs_code_new.purchase_year = rowValues[11]  # 采购时间
                    hs_code_new.save()
                    hs_code_new.clean_fields()
        except Exception as e:
            print(e)
            return render(request, 'contract_excel/hs_info_import.html', {"message": '出现错误....'})
        return redirect('/hs_code_new')
    else:
        return render(request, 'contract_excel/hs_info_import.html')


@login_check
def hs_code_new(request):
    if request.method == 'POST':
        customer = request.POST.get('custom')   # 厂家
        en_name = request.POST.get('en_name')   # 产品英文名
        zh_name = request.POST.get('zh_name')   # 产品中文名
        part_num = request.POST.get('part_num')  # 零件号
        cybm = request.POST.get('cybm') # 长裕编码
        code = request.POST.get('hs_code')  # HS编码
        sub_cra = request.POST.get('sub_cra')  #

        hs_codes_new = Harmonized_System_Customer.objects.filter(custom__contains=customer,
                                                                 goods_code__contains=cybm,
                                                                 goods_zh_name__contains=zh_name,
                                                                 part_num__contains=part_num,
                                                                 goods_en_name__contains=en_name,
                                                                 subull_crapidiary__contains=sub_cra,
                                                                 hs_code__contains=code
                                                                 )
        return render(request, 'contract_excel/hs_new.html', {'hs_codes_new': hs_codes_new})
    else:
        return render(request, 'contract_excel/hs_new.html')
