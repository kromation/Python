from django.shortcuts import render
from django.http import HttpResponse
# create your views here
# request -> response
# request handler
# action / view

def say_hello(request):
    #Pull Data from Database
    #Transform Data
    #Send Email
    return HttpResponse('Hello World')
