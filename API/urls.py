# API/urls.py
from django.urls import path
from .views import ClientAndBonusView

urlpatterns = [
    path('api/v1/client-bonus/', ClientAndBonusView.as_view(), name='client-bonus'),
]