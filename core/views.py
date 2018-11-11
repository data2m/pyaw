from django.shortcuts import render
from django.http import HttpResponse

from .models import Asset, Machine, Project

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
    sub_assets = asset.asset_parent.order_by('id')

    context = {
        'asset': asset,
        'sub_assets':sub_assets
        }
    return render(request, 'core/asset.html', context)


def machines(request):
    machines = Machine.objects.order_by('id')
    context = {'machines': machines}
    return render(request, 'core/machines.html', context)

def projects(request):
    projects = Project.objects.order_by('id')
    context = {'projects': projects}
    return render(request, 'core/projects.html', context)