from django.urls import path
from .views import ingresoList, ingresoDetail

urlpatterns = [
    path('ingreso/', ingresoList.as_view(), name='ingreso-list'),
    path('ingreso/<int:pk>/', ingresoDetail.as_view(), name='ingreso-detail'),
]