from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from gas_stations.utils import renew_gas_stations_from_api


class UpdateGasStations(APIView):

    def post(self, request, *args, **kwargs):
        created_gas_stations, updated_gas_stations = renew_gas_stations_from_api()
        return Response({"created": created_gas_stations, "updated": updated_gas_stations}, status=status.HTTP_200_OK)
