from rest_framework import serializers

from LoyalityManagement.models import Asset, AssetGroup


class AssetGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetGroup
        fields = [
            'begin',
            'end',
            'weight'
        ]

class AssetsSerializers(serializers.ModelSerializer):
    group_info=serializers.SerializerMethodField()

    class Meta:
        model = Asset
        # fields = '__all__'
        fields = [
            'id',
            'dateFromCash',
            'amount',
            'date',
            'lastStatus',
            'status',
            'assetGroupId',
            'group_info',
            'cardNumber',
            'additionalInfo',
            'lastSource',
            'lastReason'
        ]

    def get_group_info(self, obj):
        group_info = AssetGroup.objects.filter(internalId=obj.assetGroupId)
        return AssetGroupSerializer(group_info, many=True).data