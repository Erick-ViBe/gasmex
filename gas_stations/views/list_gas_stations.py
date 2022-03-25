from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework import status
from gas_stations.models import GasStation
from gas_stations.serializers import BaseGasStationSerializer
from gas_stations.utils import get_price_averages


class ListRetrieveGasStationsViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = GasStation.objects.all()
    serializer_class = BaseGasStationSerializer
    lookup_field = 'gas_station_id'

    def get_queryset(self):
        queryset = self.queryset
        zip_code = self.request.query_params.get("zip_code", None)
        if zip_code:
            queryset = queryset.filter(zip_code=zip_code)
        else:
            rfc_name = self.request.query_params.get("rfc_name", None)
            if rfc_name:
                queryset = queryset.filter(
                    Q(rfc__contains=rfc_name)
                    | Q(company_name__contains=rfc_name)
                )
        return queryset

    @action(detail=False, methods=["GET"], url_path=r'compare/(?P<first_gas_station_rfc>\w+)/(?P<second_gas_station_rfc>\w+)')
    def compare(self, request, first_gas_station_rfc, second_gas_station_rfc):
        first_gas_stations = GasStation.objects.filter(rfc=first_gas_station_rfc)
        second_gas_stations = GasStation.objects.filter(rfc=second_gas_station_rfc)
        error_rfc = []
        if not first_gas_stations:
            error_rfc.append(first_gas_station_rfc)
        if not second_gas_stations:
            error_rfc.append(second_gas_station_rfc)
        if error_rfc:
            return Response(
                {"error": {"There is no gas station with RFC": error_rfc}},
                status=status.HTTP_404_NOT_FOUND,
            )
        else:
            response = {
                first_gas_station_rfc: get_price_averages(first_gas_stations),
                second_gas_station_rfc: get_price_averages(second_gas_stations),
            }
            return Response(
                response,
                status=status.HTTP_200_OK,
            )
