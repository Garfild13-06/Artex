from django.urls import path

from LoyalityManagement.views import LmTest, LmAssets

urlpatterns = ([
    path('api/v1/lm/test/', LmTest.as_view()),
    path('api/v1/lm/assets/', LmAssets.as_view()),
])
