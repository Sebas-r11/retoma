
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sup/', include('panda.urls')),
    path('sum/', include('polar.urls')),
    path('sumcalif/', include('pardo.urls'))
]
