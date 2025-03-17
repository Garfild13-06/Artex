from django.urls import path

from LoyalityManagement.views import LmTest

urlpatterns = ([
    path('api/v1/lm/test/', LmTest.as_view()),
])
