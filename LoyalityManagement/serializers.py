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
    begin = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()
    weight = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()

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
            'begin',
            'end',
            'weight',
            'cardNumber',
            'additionalInfo',
            'lastSource',
            'lastReason'
        ]

    def get_amount(self, obj):
        return obj.amount / 100 if obj.amount else 0

    def get_begin(self, obj):
        group = AssetGroup.objects.filter(internalId=obj.assetGroupId).first()
        return group.begin if group else None

    def get_end(self, obj):
        group = AssetGroup.objects.filter(internalId=obj.assetGroupId).first()
        return group.end if group else None

    def get_weight(self, obj):
        group = AssetGroup.objects.filter(internalId=obj.assetGroupId).first()
        return group.weight if group else None
