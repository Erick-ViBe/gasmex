import json
import math
import requests
from gas_stations.models import GasStation


def renew_gas_stations_from_api():
    """
    Use this function when you need to update gas staions, either with a CRON, etc, etc.
        Response:
            - Number of new gas stations
            - Number of updated gas stations
    """
    url = "https://api.datos.gob.mx/v1/precio.gasolina.publico"
    response = requests.get(url)
    response = json.loads(response.text)
    pages = int(math.ceil(response["pagination"]["total"]/response["pagination"]["pageSize"]))
    created_gas_stations, updated_gas_stations = save_gas_stations(response["results"])
    for i in range(2, pages+1):
        response = requests.get(f"{url}?page={i}")
        response = json.loads(response.text)
        new_created_gas_stations, new_updated_gas_stations = save_gas_stations(response["results"])
        created_gas_stations += new_created_gas_stations
        updated_gas_stations += new_updated_gas_stations
    return created_gas_stations, updated_gas_stations

def save_gas_stations(gas_stations):
    created_gas_stations = 0
    updated_gas_stations = 0
    for raw_gas_station in gas_stations:
        raw_gas_station = {
            "gas_station_id": raw_gas_station["_id"],
            "address": raw_gas_station["calle"],
            "rfc": raw_gas_station["rfc"],
            "regular_gasoline_price": raw_gas_station["regular"],
            "premium_gasoline_price": raw_gas_station["premium"],
            "diesel_price": raw_gas_station["dieasel"],
            "longitude": raw_gas_station["longitude"],
            "latitude": raw_gas_station["latitude"],
            "zip_code": raw_gas_station["codigopostal"],
            "company_name": raw_gas_station["razonsocial"],
        }
        try:
            gas_station = GasStation.objects.get(gas_station_id=raw_gas_station["gas_station_id"])
            for attr, value in raw_gas_station.items():
                setattr(gas_station, attr, value)
            updated_gas_stations += 1
        except GasStation.DoesNotExist:
            gas_station = GasStation.objects.create(**raw_gas_station)
            created_gas_stations += 1

    return created_gas_stations, updated_gas_stations

def get_price_averages(gas_stations: list[GasStation]):
    price_averages = {
        "regular_gasoline": {
            "price_average": 0,
            "count": 0
        },
        "premium_gasoline": {
            "price_average": 0,
            "count": 0
        },
        "diesel": {
            "price_average": 0,
            "count": 0
        },
    }
    for gas_station in gas_stations:
        for fuel_type, data in price_averages.items():
            price = getattr(gas_station, f"{fuel_type}_price")
            if price:
                data["price_average"] = data["price_average"] + float(price)
                data["count"] = data["count"] + 1

    for data in price_averages.values():
        if data["count"]:
            data["price_average"] = round(data["price_average"] / data["count"], 2)

    price_averages["id"] = gas_stations[0].gas_station_id
    price_averages["company_name"] = gas_stations[0].company_name

    return price_averages
