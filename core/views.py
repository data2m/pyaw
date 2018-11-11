from django.shortcuts import render
from django.http import HttpResponse

from .models import Asset

def index2(request):
    return HttpResponse("Hello world! Data2m") 


def index(request):
    return render(request, 'core/index.html', {})


def assets(request):
    assets = Asset.objects.order_by('id')
    context = {'assets': assets}
    return render(request, 'core/assets.html', context)

def asset(request, asset_id):
    asset = Asset.objects.get(id=asset_id)   
    context = {'asset': asset}
    return render(request, 'core/asset.html', context)