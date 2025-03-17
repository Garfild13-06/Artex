from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class LmTest(APIView):
    def get(self, request):
        return Response({
            "status": "ok",
            "code": status.HTTP_200_OK,
            "message": "Список успешно получен",
            "data": ""
        }, status=status.HTTP_200_OK)
