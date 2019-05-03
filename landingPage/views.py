from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('<h1>landingPage Home</h1>')


def home_about(request):
    return HttpResponse('<h1>about Home</h1>')