from re import search

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from LoyalityManagement.models import Asset
from LoyalityManagement.serializers import AssetsSerializers
from utils.CustomLimitOffsetPagination import CustomLimitOffsetPagination


# Create your views here.
class LmTest(APIView):
    def get(self, request):
        return Response({
            "status": "ok",
            "code": status.HTTP_200_OK,
            "message": "Список успешно получен",
            "data": ""
        }, status=status.HTTP_200_OK)


class LmAssets(APIView):
    def post(self, request, *args, **kwargs):
        queryset = Asset.objects.all()
        card_queryset=request.data.get('card', None)
        if card_queryset:
            queryset = queryset.filter(cardNumber__exact=card_queryset).order_by('-id')
        paginator = CustomLimitOffsetPagination()
        page = paginator.paginate_queryset(queryset,request)
        serializer = AssetsSerializers(page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)