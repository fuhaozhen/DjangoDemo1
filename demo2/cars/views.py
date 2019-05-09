from django.shortcuts import render,redirect,reverse
# Create your views here.
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
# 身份认证 登出 登录（记录登录状态）
from django.contrib.auth import authenticate, logout, login
from datetime import datetime
# 分页器
from django.core.paginator import Paginator
# 发送邮件
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
# 序列化
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
# 验证码
from PIL import Image, ImageDraw, ImageFont
import random
import io
import re


def index(request):
    hotpics = Hotpic.objects.all().order_by("index")
    # print(hotpics[0].pic.url)
    for hotpic in hotpics:
        print(hotpic.pic.url)
    return render(request, 'cars/index.html', {"username": request.session.get("username"), "hotpics": hotpics})


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
            result = re.fullmatch(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', useremail)
            if result:
                # 判断两次密码是否一致
                if userpwd != re_userpwd:
                    return render(request, 'cars/register.html', {'error_code': -2, 'error_msg': "两次密码输入不一致"})
            else:
                return redirect(reverse('cars:user_register'), {"error_code": -6, 'error_msg': "邮箱格式不正确"})

        # 创建用户注册

        user = User.objects.create_user(username=username, password=userpwd, email=useremail, is_active=False)
        id = user.id
        print(id)

        # 序列化Id
        serutil = Serializer(settings.SECRET_KEY, 300)
        resultid = serutil.dumps({"id": id}).decode("utf-8")

        # print(user.email)
        send_mail("点击激活账户", "<a href='http://127.0.0.1:8000/cars/active/%s'>点击我激活账户</a>"%(resultid,), settings.DEFAULT_FROM_EMAIL, [user.email])
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
        return render(request, 'cars/login.html', {'error_code': 1, 'error_msg': "账号注册成功，请在邮箱中激活账户"})


def long(request):
    car = Car.objects.all()
    if request.method == "GET":
        return render(request, 'cars/long.html', {"carlist": car, "username": request.session.get("username")})
    elif request.method == "POST":
        return render(request, 'cars/long.html', {"carlist": car, "username": request.session.get("username")})


def short(request):
    car = Car.objects.all()
    # 分页器，一页8个
    pagor = Paginator(car, 8)
    # 页码，pagenum表示第几页
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum
    # print(pagor.object_list, pagor.page_range, pagor.num_pages, pagor.count)
    page = pagor.page(pagenum)
    # print(page.paginator, page.object_list, page.number, page.has_previous(), page.has_next())

    return render(request, 'cars/short.html', {"carlist": car,"username": request.session.get("username"), "page": page})


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
    car = Car.objects.get(pk=id)
    orders = Order.objects.all()
    return render(request, 'cars/order.html', {"car": car, "orders": orders})


def commit(request, id):
    car = Car.objects.get(pk=id)
    qutime = request.POST["qutime"]
    huantime = request.POST["huantime"]

    print(qutime)
    print(huantime,"********************************8")
    day1 = qutime.split("-")[-1]
    day2 = huantime.split("-")[-1]
    month1 = qutime.split("-")[-2]
    month2 = huantime.split("-")[-2]
    if month1 == month2:
        longtime = int(day2) - int(day1)
    else:
        longtime = 30 - int(day1) + int(day2)
    print(type(longtime))
    print(longtime)
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
    car.carnum -= 1
    car.save()
    # print(car, type(car), "#########")
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

    print(order1.returnDate, "************************")
    print(type(order1.returnDate))
    order1.otime = request.POST["longtime"]
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
    picture = newuser.customer.picture
    return render(request, 'cars/me.html', {"carlist": car, "username": user1, "newuser": newuser, "picture": picture})


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
    if request.method == "GET":
        return render(request, "cars/xiugai.html")
    elif request.method == "POST":
        new1 = request.session.get("username")
        news = User.objects.get(username=new1)
        news.email = request.POST["email"]
        print(type(news))
        news.customer.tel = request.POST["tel"]
        news.customer.age = request.POST["age"]
        news.customer.addr = request.POST["addr"]
        news.customer.gender = request.POST["inlineRadioOptions"]
        news.customer.picture = request.FILES["pic"]

        news.customer.save()
        news.save()
        print(news.customer.picture)
        return redirect('/cars/me/')


def advice(request):
    if request.method == "GET":
        return render(request, 'cars/login.html')
    elif request.method == "POST":
        user1 = request.session["username"]
        users = User.objects.get(username=user1)
        users.customer.description = request.POST["car_style"]
        users.customer.tel = request.POST["tel"]
        users.customer.addr = request.POST["addr"]
        users.customer.save()
        users.save()
        return render(request, 'cars/success.html', {"users": users})


def success(request):
    advice1 = Advice()
    advice1.name = request.POST["username"]
    advice1.gender = request.POST["gender"]
    advice1.email = request.POST["email"]
    advice1.phone = request.POST["tel"]
    advice1.title = request.POST["title"]
    advice1.content = request.POST["comment"]
    advice1.save()
    return render(request, 'cars/success.html')


def header(request):
    return render(request, 'cars/header.html')


def reset(request):
    name = request.POST["username"]
    tel = request.POST["tel"]
    # 验证码
    verifycode = request.POST["verifycode"]
    try:
        user = User.objects.get(username=name)
        if user and user.customer.tel == tel:
            # return render(request, 'cars/reset.html', {"user": user})
            if verifycode == request.session.get("verifycode"):
                # print(user, type(user))
                return render(request, 'cars/reset.html', {"user": user})
            else:
                return render(request, 'cars/header.html', {"user": user, "error_code": -3, "error_msg": "验证码错误"})
        else:
            return render(request, 'cars/header.html', {"error_code": -4, "error_msg": "用户名或手机号有误"})
    except:
        return HttpResponse("出错了")


def changes(request):
    user = request.POST["username"]
    # print(user)
    try:
        users = User.objects.get(username=user)
        newpsw = request.POST["psw"]
        re_newpsw = request.POST["re_psw"]
        if newpsw == re_newpsw:
            users.set_password(newpsw)
            users.save()
            return render(request, 'cars/changes.html')
        else:
            return render(request, 'cars/reset.html', {"error_code": 1, "error_msg": "两次密码输入不一致"})
    except:
        return render(request, 'cars/reset.html')


def email(request):
    """发送邮件"""
    try:
        send_mail("Django发送邮件", "Django自带邮件功能，你可以使用sen_mail发送，<a herf='http://127.0.0.1:8000/'></a>", settings.DEFAULT_FROM_EMAIL, ["1542242578@qq.com"])
        return HttpResponse("发送成功")
    except Exception as e:
        print(e)
        return HttpResponse("发送失败")


def active(request, idstr):
    # user = User.objects.get(pk=id)
    # user.is_active = True
    # user.save()
    # return redirect(reverse('cars:user_login'), {"error_code": 3, "error_msg": "账号激活成功，请登录"})
    deser = Serializer(settings.SECRET_KEY, 300)
    try:
        obj = deser.loads(idstr)
        user = User.objects.get(pk=obj["id"])
        user.is_active = True
        user.save()
        return render(request, 'cars/login.html', {"error_code": 3, "error_msg": "账号激活成功，请登录"})
    except:
        return HttpResponse("链接失效")


def checkuser(request):

    if request.method == "POST":
        username = request.POST["username"]
        user = User.objects.filter(username=username).first()
        if user is None:
            return HttpResponse("用户名不存在")
        else:
            return HttpResponse("ok")


def verifycode(request):
    # 生成验证码图片
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 105
    heigth = 50
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
    fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
    draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('Lobster-Regular.ttf', 24)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((7, 12), rand_str[0], font=font, fill=fontcolor)
    draw.text((27, 12), rand_str[1], font=font, fill=fontcolor)
    draw.text((52, 12), rand_str[2], font=font, fill=fontcolor)
    draw.text((77, 12), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw

    # 将生成的验证码存入session
    request.session['verifycode'] = rand_str.lower()

    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')


def ajaxload(request):
    return render(request, 'cars/ajaxload.html')


def ajax(request):
    if request.method == "GET":
        return HttpResponse("get请求成功")
    elif request.method == "POST":
        return HttpResponse("post请求成功")

