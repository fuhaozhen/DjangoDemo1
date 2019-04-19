from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    question = Question.objects.all()
    return render(request, "polls/index.html", {"questions": question})


def detail(request, id):
    q = Question.objects.get(pk=id)
    return render(request, "polls/detail.html", {"q": q})


def vote(request, id):
    cid = request.POST["choice"]
    c = Choice.objects.get(pk=cid)
    c.cvote += 1
    c.save()
    q = Question.objects.get(pk=id)
    return render(request, "polls/vote.html", {"choices": q.choice_set.all(), "q": q})

