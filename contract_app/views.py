from django.shortcuts import render, redirect
from suds.client import Client, sudsobject
from contract_app.models import User
from django.contrib import messages  # 需要导的包
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator


# Create your views here.

def login_check(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.has_key('is_login'):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/login')
    return wrapper


def get_contract(contract):
    user_url = 'http://erpep.ytcg.cn:8000/sap/bc/srt/wsdl/' \
               'srvc_005056AF3AB11ED9AB8A67D6754781BA/wsdl11' \
               '/allinone/ws_policy/document?sap-client=800'
    # user_url = 'http://ERPDEV.ytcg.cn:8000/sap/bc/srt/wsdl/srvc_' \
    #            '005056AF2A111ED9AA87283B45BF1437/wsdl11/allinone/' \
    #            'ws_policy/document?sap-client=120'
    client = Client(user_url, username='RFCUSER', password='cybl@123')
    # print(client)
    result = client.service.ZchyFmHt001(contract)
    # print(result)
    return result


def recursive_dict(d):
    out = {}
    for k, v in sudsobject.asdict(d).items():
        if hasattr(v, '__keylist__'):
            out[k] = recursive_dict(v)
        elif isinstance(v, list):
            out[k] = []
            for item in v:
                if hasattr(item, '__keylist__'):
                    out[k].append(recursive_dict(item))
                else:
                    out[k].append(item)
        else:
            out[k] = v
    return out

@login_check
def index(request):
    contract = request.POST.get('contract')
    # print(type(contract))
    # print('cntract', contract)
    if contract is not None:
        # print(contract)
        result = get_contract(contract)
        # print(result)
        result = recursive_dict(result)
        # print(type(result))
        # print(result)
        # print(result.keys())
        # print(result)'
        result1 = result.get('THt001')
        if result1:
            # print('note')
            result1 = result1.get('item')
        result2 = result.get('THt002')
        if result2:
            result2 = result2.get('item')
        result3 = result.get('THt003')
        if result3:
            result3 = result3.get('item')
        result4 = result.get('THt004')
        if result4:
            result4 = result4.get('item')
        total_pages = 31

        # print(result)
        return render(request, 'contract_app/index.html',
                      {'contracts': result1,
                       'fks': result2,
                       'ztds': result3,
                       'zdls': result4})
    else:
        return render(request, 'contract_app/index.html')


def register(request):
    return render(request, 'contract_app/register.html')


# 注册用户写入数据库
def user_create(**kwargs):
    user = User()
    user.username = kwargs.get('username')
    user.department = kwargs.get('dep')
    user.email = kwargs.get('email')
    user.password = make_password(kwargs.get('pwd1'))
    user.save()


# *注册账号检查
def register_check(request):
    # 获取post值
    username = request.POST.get('username')
    dep = request.POST.get('dep')
    email = request.POST.get('email')
    pwd1 = request.POST.get('pwd1')
    pwd2 = request.POST.get('pwd2')
    # 根据获取的值去数据库读取，看是否已经注册
    names = User.objects.filter(username=username)
    emails = User.objects.filter(email=email)

    # 判断两次输入的密码是否一致
    # print(pwd1)
    # print(pwd2)
    if pwd1 == pwd2:
        if names or emails:
            # print('用户名或邮箱已注册！')
            # message = '用户名或邮箱已注册！'
            messages.add_message(request, messages.WARNING, "用户名或邮箱已注册！")
            return redirect('/register')
        else:
            user_dict = {'username': username,
                         'dep': dep,
                         'email': email,
                         'pwd1': pwd1}
            user_create(**user_dict)
            return redirect('/login')
    else:
        messages.add_message(request, messages.WARNING, "两次输入的密码不一致！")
        return redirect('/register')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')
    if request.method == 'POST':
        user = User()
        username = request.POST.get('username')
        pwd1 = request.POST.get('pwd1')
        if username is not None:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                messages.add_message(request, messages.ERROR, "输入的用户名不存在，请重新输入！")
                return render(request, 'contract_app/login.html')

        if check_password(pwd1, user.password):
            request.session['is_login'] = True
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('/index')
        else:
            # messages.add_message(request, messages.ERROR, "输入的密码错误，请重新输入！")
            message = "输入的密码错误，请重新输入！"
            return render(request, 'contract_app/login.html', {"message": message})
    else:
        return render(request, 'contract_app/login.html')


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login")


def reset(request):
    user_change = User()
    user_name = request.POST.get('username')
    pwd1 = request.POST.get('pwd1')
    pwd2 = request.POST.get('pwd2')
    if request.method == 'POST':
        if pwd1 == pwd2:
            try:
                user = User.objects.get(username=user_name)
                user_change.username = user_name
                user_change.department = user.department
                user_change.email = user.email
                user_change.password = make_password(pwd1)
                user.delete()
                user_change.save()
                messages.add_message(request, messages.ERROR, "重置成功！")
                return render(request, 'contract_app/jump.html')
            except User.DoesNotExist:
                messages.add_message(request, messages.ERROR, "输入的用户名不存在，请重新输入！")
                return render(request, 'contract_app/reset.html')
        else:
            messages.add_message(request, messages.WARNING, "两次输入的密码不一致！")
            return render(request, 'contract_app/reset.html')
    else:
        return render(request, 'contract_app/reset.html')
