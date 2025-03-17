from django.urls import path

from ControlCenter.views import CCTest

urlpatterns = ([
    path('api/v1/cc/test/', CCTest.as_view()),
])
