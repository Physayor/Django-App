from django.shortcuts import render
from django.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Yayyyyy')
