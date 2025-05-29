from django.shortcuts import render
from django.http import HttpResponse

def cart(request):
    return HttpResponse("Here you can buy a lot of games.")