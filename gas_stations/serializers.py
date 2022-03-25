from rest_framework import serializers
from gas_stations.models import GasStation


class BaseGasStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasStation
        fields = [
            'gas_station_id',
            'address',
            'zip_code',
            'rfc',
            'regular_gasoline_price',
            'premium_gasoline_price',
            'diesel_price',
            'longitude',
            'latitude',
            'company_name',
        ]
