# Django
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status

# Models
from apps.summary.models.summary import Summary

# Serializers
from apps.summary.serializers.summary_serializer import SummarySerializer

# Methods
from apps.summary.methods.calendar import Calendar
from apps.summary.methods.filter import Filter


CUSTOM_TOKEN = ({
  "credentials": "{\"SSO_ID\": \"v1.2~1~ADC50289B63AD5D6BCBE080BD729EAC62F41451CEC4438D77F8683CBC5DAA76AB1432067C46DB8F4142A5C8CB55DCA22A81199E0D2EC7E4C9B3750AC18A07A46028E4532DEF7B637B68F671C7D24EE96D4705634FD66E21524EE1D6CAE48015A5D78749ACF2D3D04A3236D98CB159F519711C3AD76285BA9A3C9C1A162CC6614B2D1D45D800C24B2F94A14B6FD2C55C0833BC68613E33B2FF4F951884AA90135C30D53DDAAFB13A35E30F52F0E64D64CA4B268A1470DF1DB451E872CA1A4E68A9982E6A83FC111B7079F9561FCAC18FD3D912E229871A11DF6B2C193AD0371A46B2183D08471247364732CE15564EBBCC1C33829E9254A57\", \"portal\": \"9.0.3+en-us+us+AMERICA+0980D5EB85E47B78E06015AC19C86AE9+DADCF758C19F78BAB5AD3E57D466D2A89E293BD6A84309856308066AE85F22DAF529EF3F5576561C55C8713DB58767C62C3DB54A3A95748CFCD5516BF1E447947185CCDFC6DF3FC088C51AB41D86A62B1424231B28B280EF\", \"portal_url\": \"\"}",
  "user": "1193096338",
  "password": "123amarillo"
})


class SummaryViewSet(GenericViewSet):

    serializer_class = SummarySerializer
    queryset = Summary.objects.all()

    def list(self, request) -> (Response):
        calendar = Calendar(CUSTOM_TOKEN)
        filter_data = Filter(data=calendar.get_class()).filter(
            week_days=calendar.get_calendar_days(), all=True)

        if not filter_data:
            return Response("", status=status.HTTP_400_BAD_REQUEST)

        return Response("All ok ;)")
