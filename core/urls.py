from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('assets/', views.assets, name='assets'),
    path('assets/<asset_id>/', views.asset, name = 'asset')
]
