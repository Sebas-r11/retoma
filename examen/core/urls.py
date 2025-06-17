
from django.contrib import admin
from django.urls import path, include
from basico import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('basico.urls')),
    path('apidos/', include('dost.urls')),
    path('apitres/', include('trest.urls')),
]
