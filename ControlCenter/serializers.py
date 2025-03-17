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
    cards = serializers.SerializerMethodField()

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
            'cards']

    def get_cards(self, obj):
        cards = CardTemp.objects.filter(idclient=obj.idclient)
        return CardTempSerializer(cards, many=True).data
