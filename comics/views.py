from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the comics index.")


def detail(request, people_id):
    return HttpResponse("You're looking at comic %s." % people_id)


def results(request, people_id):
    response = "You're looking at the results of comic %s."
    return HttpResponse(response % people_id)


def vote(request, people_id):
    return HttpResponse("You're voting on comic %s." % people_id)
