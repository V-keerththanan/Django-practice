from cgitb import html
from http.client import HTTPResponse
from re import template
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    cont={'name':'keerththanan'}
    return render(request,"sample.html",context=cont)

def sayWelcome(request):
    return HttpResponse("Hi welcome you!")