# Django
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status

# Models
from apps.califications.models.calification import Calification

# Serializers
from apps.califications.serializers.calification_serializer import CalificationSerializer

# Methods
from apps.califications.methods.califications import Califications


CUSTOM_TOKEN = ({
            "credentials": "{\"SSO_ID\": \"v1.2~1~6B942BE548F369760491796D1177B717900579B6D8F2B45C37F3B02E4219E96687114E09DB78C17E1784533CC5B37E91A8A123823B007F1A486C010CEF7D97C86FF9D7334113310854F78AB3571F0D0A652B31D49F8665BC70FA3FEC453B7B003B347501DDCE4EC51350AAB76D76F83317E18B37E3AD4D24B9F3EB38800A0E0EDF7BE2E60ADD257B45BC25CA735DFE36D3E2FF1C949F3DA77D48DCCF39221F0C2ECC64C3E8C3DF98005871364326F1577C5C07D74C54642EA8C0B52964F69D42E3DBBC9D2DABB816267373A30E717179EB1149E8F87CFD1AE3BB8A1418CF601372B6C1C256616F60952B06A33FD4C6EDB7241AB0DB18DCAF\", \"portal\": \"9.0.3+en-us+us+AMERICA+092E09477EE04A8AE06015AC19C83C3E+4351A0E91A0EFF3B0919A963B6CBC916CA3B5BBD9161F52C3E4FAFDD2CC7C685A175456058D19D5F6633CFF51E839D1EE941985AAF17A5338A57795221B6D24CA4D87929836C2D185929EE9A22697995E7DF30EEC955FC40\", \"portal_url\": \"\"}",
            "user": "1104124494",
            "password": "1104124494cala"
        })

class CalificationViewSet(GenericViewSet):

    serializer_class = CalificationSerializer
    queryset = Calification.objects.all()

    def list(self, request) -> (Response):
        califications = Califications(CUSTOM_TOKEN)
        options_list = califications.options()
        return Response("Hello all califications")
