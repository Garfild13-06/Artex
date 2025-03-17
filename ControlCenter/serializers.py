from rest_framework import serializers

from ControlCenter.models import ClientTemp


class ClientTempSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientTemp
        fields = '__all__'