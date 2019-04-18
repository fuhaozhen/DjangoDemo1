"""
视图函数，将函数和路由绑定
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import BookInfo, HeroInfo
from django.template import loader, RequestContext
# Create your views here.


def index(request):
    # # return HttpResponse("首页")
    # # 1加载模板
    # indextem = loader.get_template("booktest/index.html")
    #
    # # 2使用变量参数渲染模板
    # result = indextem.render({"username": "zzy"})
    #
    # # 3返回模板
    # return HttpResponse(result)
    b1 = BookInfo.objects.all()
    return render(request, "booktest/index.html", {"booklist": b1})


def list(request):
    b1 = BookInfo.objects.all()
    return render(request, "booktest/list.html", {"booklist": b1})


def detail(request, id):
    # try:
    #     name = BookInfo.objects.get(pk=int(id)).btitle
    #     return HttpResponse("详情页"+name)
    # except Exception as e:
    #     print(e)
    b1 = BookInfo.objects.get(pk=id)
    return render(request, "booktest/detail.html", {"book": b1})
    # 重定向
    # return HttpResponseRedirect("booktest/detail.html", {"book": b1})


def add(request):
    bname = request.POST["bname"]
    book = BookInfo()
    book.btitle = bname
    book.save()
    b1 = BookInfo.objects.all()
    return render(request, "booktest/list.html", {"booklist": b1})


def delete(request, id):
    try:
        BookInfo.objects.get(pk=id).delete()
        b1 = BookInfo.objects.all()
        return render(request, "booktest/list.html", {"booklist": b1})
    except:
        return HttpResponse("删除成功")


def addhero(request, bookid):
    b1 = BookInfo.objects.get(pk=bookid).btitle
    return render(request, "booktest/addhero.html", {"bookid": bookid, "btitle": b1})


def addherohandler(request):
    bookid = request.POST["bookid"]
    hname = request.POST["heroname"]
    hgender =request.POST["gender"]
    hconent = request.POST["herocontent"]
    book = BookInfo.objects.get(pk=bookid)

    hero = HeroInfo()
    hero.hname = hname
    hero.hgender = hgender
    hero.hcontent = hconent
    hero.hbook = book

    hero.save()

    # booktest前面忘了加/，表示从域名后开始
    return HttpResponseRedirect("/booktest/detail/"+str(bookid), {"book": book})
    # return  HttpResponseRedirect("添加成功")


# def deletehero(request):
#     return HttpResponse("删除成功")




