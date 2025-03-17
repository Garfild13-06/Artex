from re import search

from django.shortcuts import render
from rest_framework.views import APIView

from ControlCenter.models import ClientTemp
from ControlCenter.serializers import ClientTempSerializer
from utils.CustomLimitOffsetPagination import CustomLimitOffsetPagination


# Create your views here.
class CCTest(APIView):
    def post(self, request, *args, **kwargs):
        queryset = ClientTemp.objects.all()
        search_query = request.data.get('search', None)
        if search_query:
            queryset = queryset.filter(phonenumber__contains=search_query)
            paginator = CustomLimitOffsetPagination()
            page = paginator.paginate_queryset(queryset, request)
            serializer = ClientTempSerializer(page, many=True, context={'request': request})
            return paginator.get_paginated_response(serializer.data)
