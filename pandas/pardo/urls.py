from django.urls import path
from .views import calificadorList, calificadorDetail

urlpatterns = [
    path('calificador/', calificadorList.as_view(), name='calificador-list'),
    path('calificador/<int:pk>/', calificadorDetail.as_view(), name='calificador-detail'),
]