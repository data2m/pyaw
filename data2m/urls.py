from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from material.frontend import urls as frontend_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    url(r'', include(frontend_urls)),
]
