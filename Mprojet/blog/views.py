from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text = "<h1> Je suis heureux de coder avec django</h1>"
    return HttpResponse(text)
