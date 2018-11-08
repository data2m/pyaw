from django.shortcuts import render
from django.http import HttpResponse

def index2(request):
    return HttpResponse("Hello world! Data2m") 


def index(request):
    return render(request, 'core/index.html', {})

