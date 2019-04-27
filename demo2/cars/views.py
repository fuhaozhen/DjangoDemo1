from django.shortcuts import render,redirect,reverse
# Create your views here.
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
# 身份认证 登出 登录（记录登录状态）
from django.contrib.auth import authenticate, logout, login
from datetime import date

def index(request):
    if request.method == "GET":
        return render(request, 'cars/index.html', {"username": request.session.get("username")})
    elif request.method == "POST":
        return render(request, 'cars/index.html', {"username": request.session.get("username")})


def user_login(request):
    if request.method == "GET":
        return render(request, 'cars/login.html')
    elif request.method == "POST":
        # 获取数据
        username = request.POST["username"]
        userpwd = request.POST["userpwd"]

        # 判断验证
        user = authenticate(username=username, password=userpwd)
        if user is not None:

            # 验证账号是否锁定
            if user.is_active:
                # 记录登录状态，跳转页面
                login(request, user)
                request.session["username"] = username
                return render(request, 'cars/index.html', {"error_code": 1, "error_msg": "登录成功", "username":username})
            else:
                return render(request, 'cars/login.html', {"error_code": -1, "error_msg": "账号或密码有误"})
        else:
            return render(request, 'cars/login.html', {"error_code": -1, "error_msg": "账号或密码有误"})


def user_register(request):
    if request.method == "GET":
        return render(request, 'cars/register.html')
    elif request.method == "POST":
        # 获取用户数据
        username = request.POST["username"]
        usertel = request.POST["usertel"]
        userpwd = request.POST["userpwd"]
        re_userpwd = request.POST["re_userpwd"]
        useremail = request.POST["useremail"]

        # 判断账号是否可用
        try:
            user = User.objects.get(username=username)
            return render(request, 'cars/register.html', {'error_code': -1, 'error_msg': "账号已存在，请使用其他账号注册"})
        except:
            # 判断两次密码是否一致
            if userpwd != re_userpwd:
                return render(request, 'cars/register.html', {'error_code': -2, 'error_msg': "两次密码输入不一致"})

        # 创建用户注册
        user = User.objects.create_user(username=username, password=userpwd, email=useremail)
        customer = Customer()
        customer.tel = usertel
        customer.gender = "待完善"
        customer.idCard = "待完善"
        customer.addr = "待完善"
        customer.description = "待完善"
        customer.user = user
        # user.save()
        customer.save()
        # 返回登录页面
        return render(request, 'cars/login.html', {'error_code': 1, 'error_msg': "账号注册成功，请使用新账号登录"})


def long(request):
    car = Car.objects.all()
    if request.method == "GET":
        return render(request, 'cars/long.html', {"carlist": car, "username": request.session.get("username")})
    elif request.method == "POST":
        return render(request, 'cars/long.html', {"carlist": car, "username": request.session.get("username")})


def short(request):
    car = Car.objects.all()
    return render(request, 'cars/short.html', {"carlist": car,"username": request.session.get("username")})


def shangwu(request):
    car = Car.objects.all()
    if request.method == "GET":
        return render(request, 'cars/shangwu.html', {"carlist": car, "username": request.session.get("username")})
    elif request.method == "POST":
        return render(request, 'cars/shangwu.html', {"carlist": car, "username": request.session.get("username")})


def hunqing(request):
    car = Car.objects.all()
    if request.method == "GET":
        return render(request, 'cars/hunqing.html', {"carlist": car, "username": request.session.get("username")})
    elif request.method == "POST":
        return render(request, 'cars/hunqing.html', {"carlist": car, "username": request.session.get("username")})


def daba(request):
    car = Car.objects.all()
    return render(request, 'cars/daba.html', {"carlist": car, "username": request.session.get("username")})


def guide(request):
    car = Car.objects.all()
    if request.method == "GET":
        return render(request, 'cars/guide.html', {"carlist": car, "username": request.session.get("username")})
    elif request.method == "POST":
        return render(request, 'cars/guide.html', {"carlist": car, "username": request.session.get("username")})


def about(request):
    car = Car.objects.all()
    if request.method == "GET":
        return render(request, 'cars/about.html', {"carlist": car, "username": request.session.get("username")})
    elif request.method == "POST":
        return render(request, 'cars/about.html', {"carlist": car, "username": request.session.get("username")})


def order(request, id):
    if request.method == "GET":
        car = Car.objects.get(pk=id)
        orders = Order.objects.all()
        return render(request, 'cars/order.html', {"car": car, "orders": orders})
    else:
        print("出错了")


def commit(request, id):
    car = Car.objects.get(pk=id)
    qutime = request.POST["qutime"]
    huantime = request.POST["huantime"]
    longtime = int(huantime.split("-")[-1])-int(qutime.split("-")[-1])
    # print(longtime)
    dprice = car.drentprice
    rentprice = dprice * longtime
    baoprice = 50 * longtime
    shouprice = 1 * longtime
    gpsprice = 10 * longtime
    orderprice = rentprice+baoprice+shouprice+gpsprice
    return render(request, 'cars/commit.html', {"car": car, "username": request.session.get("username"), "qutime": qutime,\
     "huantime": huantime, "longtime": longtime, "rentprice": rentprice, "baoprice": baoprice, "shouprice": shouprice,\
     "gpsprice": gpsprice, "orderprice": orderprice})


def log_out(request):
    logout(request)
    return render(request, 'cars/index.html', {"error_code": 2, "error_msg": "账号成功退出"})


def userinfo(request):
    return render(request, 'cars/userinfo.html')


def pay(request, id):
    car = Car.objects.get(pk=id)
    print(car, type(car), "#########")
    realname = request.POST["realname"]
    gender = request.POST["gender"]
    idCard = request.POST["idCard"]
    user = request.session.get("username")
    users = User.objects.get(username=user)
    users.last_name = realname[:1]
    users.first_name = realname[1:]

    users.customer.gender = gender
    users.customer.idCard = idCard
    users.customer.save()
    users.save()

    # 生成订单
    order1 = Order()
    order1.o_uid = users
    order1.customerName = realname
    order1.customerTel = users.customer.tel
    order1.o_cid = car
    order1.typeNo = car.typeNo
    order1.creatDate = request.POST["getdate"]
    # print(order1.creatDate)
    order1.returnDate = request.POST["redate"]
    order1.ocost = request.POST["priceCount"]
    # print(order1.ocost)
    order1.save()
    return render(request, 'cars/pay.html', {"car": car})


def service(request):
    car = Car.objects.all()
    return render(request, 'cars/service.html', {"carlist": car, "username": request.session.get("username")})
    
   
def online(request):
    car = Car.objects.all()
    return render(request, 'cars/online.html', {"carlist": car, "username": request.session.get("username")})


def me(request):
    car = Car.objects.all()
    user1 = request.session.get("username")
    newuser = User.objects.get(username=user1)
    return render(request, 'cars/me.html', {"carlist": car, "username": user1, "newuser": newuser})


def dingdan(request):
    user = request.session.get("username")
    user1 = User.objects.get(username=user)
    # print(user1, type(user1),"*********")
    order1 = user1.order_set.all()
    length = len(order1)
    # print(type(order1))
    return render(request, 'cars/dingdan.html', {"username": user, "order1": order1, "length": length})


def xiugai(request):
    return render(request, 'cars/xiugai.html', {"username": request.session.get("username")})


def new(request):
    new1 = request.session.get("username")
    news = User.objects.get(username=new1)
    news.email = request.POST["email"]
    news.customer.tel = request.POST["tel"]
    news.customer.age = request.POST["age"]
    news.customer.addr = request.POST["addr"]
    news.customer.gender = request.POST["inlineRadioOptions"]

    news.customer.save()
    news.save()
    # print(type(news))
    return redirect('/cars/me/')


def advice(request):
    # 新建一个用户
    user = User()
    user.username=request.POST["username"]
    user.tel = request.POST["tel"]
    user.addr = request.POST["addr"]
    user.save()

    return render(request, 'cars/advice.html')
