from rest_framework import serializers

from ControlCenter.models import ClientTemp, CardTemp


class CardTempSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardTemp
        fields = [
            # 'idcard',
            'number',
            # 'cardstatus',
            # 'update_time'
        ]


class ClientTempSerializer(serializers.ModelSerializer):
    card = serializers.SerializerMethodField()

    class Meta:
        model = ClientTemp
        fields = [
            'idclient',
            'name',
            'birthday',
            'specialdate1',
            'specialdate1name',
            'email',
            'phonenumber',
            'createdate',
            'update_time',
            'card']

    def get_card(self, obj):
        card = CardTemp.objects.filter(idclient=obj.idclient).first()
        # return CardTempSerializer(cards, many=True).data
        return card.number if card else None
