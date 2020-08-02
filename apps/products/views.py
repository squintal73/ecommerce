from django.http import HttpResponse
from django.shortcuts import render

def home_page(resquest):
    return HttpResponse('OLA')