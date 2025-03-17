# API/serializers.py
from datetime import datetime

from rest_framework import serializers
from ControlCenter.models import ClientTemp, CardTemp
from LoyalityManagement.models import Asset, AssetGroup
from LoyalityManagement.serializers import AssetsSerializers

class ClientTempSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientTemp
        fields = ['idclient', 'name', 'phonenumber']

class CardTempSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardTemp
        fields = ['number', 'cardstatus', 'discountpercent', 'purchases']

class ClientAndBonusSerializer(serializers.Serializer):
    client = ClientTempSerializer()
    card = CardTempSerializer()
    bonuses = AssetsSerializers(many=True)
    active_bonuses = serializers.SerializerMethodField()

    def get_active_bonuses(self, obj):
        # Получаем номер карты клиента
        card_number = obj['card']['number']
        today = datetime.now().date()

        # Находим группы активов, у которых end <= сегодняшней даты
        valid_groups = AssetGroup.objects.filter(end__date__lte=today).values_list('internalId', flat=True)

        # Фильтруем бонусы: статус Add и валидные группы
        active_bonuses = Asset.objects.filter(
            cardNumber=card_number,
            status='Add',
            assetGroupId__in=valid_groups
        )

        # Исключаем потраченные бонусы (те, у которых есть запись со статусом Spent и тем же assetGroupId)
        spent_groups = Asset.objects.filter(
            cardNumber=card_number,
            status='Spent'
        ).values_list('assetGroupId', flat=True)

        active_bonuses = active_bonuses.exclude(assetGroupId__in=spent_groups)

        # Возвращаем количество актуальных бонусов
        return active_bonuses.count()