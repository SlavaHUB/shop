from django.urls import path
from shop.views import catalog

urlpatterns = [
    path('', catalog),
]