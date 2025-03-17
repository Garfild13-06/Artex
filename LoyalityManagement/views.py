from datetime import datetime
from re import search

from django.db.models import OuterRef, Subquery
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from LoyalityManagement.models import Asset, AssetGroup
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
        # Базовый queryset
        queryset = Asset.objects.all()

        # Получение параметров из запроса
        card_queryset = request.data.get('card', None)
        filter_end_date = request.data.get('filter_end_date', None)

        # Фильтрация по номеру карты, если указан
        if card_queryset:
            queryset = queryset.filter(cardNumber__exact=card_queryset)

        # Фильтрация по дате окончания
        if filter_end_date:
            try:
                # Преобразование строки даты в объект datetime
                filter_date = datetime.strptime(filter_end_date, '%Y-%m-%d')
                print(filter_date)

                # Подзапрос для получения end из AssetGroup
                end_subquery = AssetGroup.objects.filter(internalId=OuterRef('assetGroupId')).values('end')[:1]

                # Аннотируем queryset значением end из AssetGroup
                queryset = queryset.annotate(group_end=Subquery(end_subquery))

                # Фильтруем: оставляем только активы с group_end < filter_date
                queryset = queryset.filter(group_end__gt=filter_date)
            except ValueError:
                return Response(
                    {"error": "Неверный формат даты для 'filter_end_date'. Используйте 'YYYY-MM-DD'."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Сортировка по убыванию ID
        queryset = queryset.order_by('-id')

        # Пагинация
        paginator = CustomLimitOffsetPagination()
        page = paginator.paginate_queryset(queryset, request)

        # Сериализация данных
        serializer = AssetsSerializers(page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
