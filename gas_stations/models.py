import uuid
from django.db import models


class GasStation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gas_station_id = models.CharField("Identificador de Gasolinera", max_length=24)
    address = models.TextField("Direccion")
    rfc = models.CharField("RFC", max_length=12)
    regular_gasoline_price = models.CharField("Precio de gasolina regular", max_length=16, null=True, blank=True)
    premium_gasoline_price = models.CharField("Precio de gasolina premium", max_length=16, null=True, blank=True)
    diesel_price = models.CharField("Precio de gasolina premium", max_length=16, null=True, blank=True)
    longitude = models.CharField("Longitud", max_length=16)
    latitude = models.CharField("Latitud", max_length=16)
    zip_code = models.CharField("Codigo Postal", max_length=5)
    company_name = models.CharField("Razon Social", max_length=255)
