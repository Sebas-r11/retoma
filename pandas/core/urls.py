from django.contrib import admin
from django.urls import path, include
from .views import home


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('sup/', include('panda.urls')),
    path('sum/', include('polar.urls')),
    path('sumcalif/', include('pardo.urls'))
]
