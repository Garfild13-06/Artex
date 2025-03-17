from datetime import datetime
from django.db.models import Sum
from rest_framework import serializers
from ControlCenter.models import ClientTemp, CardTemp
from LoyalityManagement.models import Asset, AssetGroup
from LoyalityManagement.serializers import AssetsSerializers
from ControlCenter.serializers import ClientTempSerializer, CardTempSerializer

class ClientAndBonusSerializer(serializers.Serializer):
    client = ClientTempSerializer()
    # card = CardTempSerializer()
    active_bonuses_sum = serializers.SerializerMethodField()
    bonuses = AssetsSerializers(many=True)

    def get_active_bonuses_sum(self, obj):
        # Получаем номер карты клиента
        card_number = obj['card'].number
        today = datetime.now().date()

        # Находим валидные группы активов (end <= сегодняшней даты)
        valid_groups = AssetGroup.objects.filter(end__date__gte=today).values_list('internalId', flat=True)

        # Фильтруем бонусы: валидные группы
        active_bonuses = Asset.objects.filter(
            cardNumber=card_number,
            # status='Add',
            assetGroupId__in=valid_groups
        )

        # Подсчитываем сумму поля amount
        total_sum = active_bonuses.aggregate(total=Sum('amount'))['total']/100 or 0
        return total_sum