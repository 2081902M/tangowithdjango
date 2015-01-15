from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world! <br/> <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. This tutorial has been put together by Nicole Munro, 2081902 <a href=\"/rango/\">Index</a>")
