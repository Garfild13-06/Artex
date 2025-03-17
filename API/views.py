from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ControlCenter.models import ClientTemp, CardTemp
from LoyalityManagement.models import Asset
from API.serializers import ClientAndBonusSerializer

class ClientAndBonusView(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phonenumber')
        if not phone_number:
            return Response({"error": "Номер телефона обязателен"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            client = ClientTemp.objects.get(phonenumber__contains=phone_number)
            card = CardTemp.objects.get(idclient=client.idclient)
            bonuses = Asset.objects.filter(cardNumber=card.number).order_by('-id')

            # Передаем объекты моделей в сериализатор
            data = {
                'client': client,
                'card': card,
                'bonuses': bonuses
            }
            serializer = ClientAndBonusSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ClientTemp.DoesNotExist:
            return Response({"error": "Клиент не найден"}, status=status.HTTP_404_NOT_FOUND)
        except CardTemp.DoesNotExist:
            return Response({"error": "Карта не найдена"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"Произошла ошибка: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)