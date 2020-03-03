import requests
import json
from datetime import datetime

url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/"

querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqZWNyZXNwb21AZ21haWwuY29tIiwianRpIjoiMjUyYjk2OTAtNzI1Yi00OTEzLTlkYmEtZTczMjY0ZDg5OTUzIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE1ODMyMjk5MDUsInVzZXJJZCI6IjI1MmI5NjkwLTcyNWItNDkxMy05ZGJhLWU3MzI2NGQ4OTk1MyIsInJvbGUiOiIifQ.gMxjlUTd7CM3fc3F0_lAXXGnrDyFAB-GBSEpD6CLetA"}

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

y = json.loads(response.text)

url_estaciones = y["datos"]

estaciones = requests.request("GET", url_estaciones, headers=headers)

print(estaciones.text)

estaciones_json=json.loads(estaciones.text)

indicativo_log = ''

for estacion in estaciones_json:
	if estacion["provincia"] == "LA RIOJA":
		print(estacion["nombre"], estacion["indicativo"])
		indicativo_log = estacion["indicativo"]

now = datetime.now()
date_time_sup = now.strftime("%Y-%m-%dT%H:%M:%SUTC")
date_time_inf = now.strftime("%Y-%m-%dT00:00:00UTC")

date_time_sup = "2020-03-02T00:00:00UTC"
date_time_inf = "2020-02-26T00:00:00UTC"

url_valores_climaticos = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/" + date_time_inf + "/fechafin/" + date_time_sup + "/estacion/" + indicativo_log

valores_climaticos = requests.request("GET", url_valores_climaticos, headers=headers, params=querystring)

print(valores_climaticos.text)

valores_json=json.loads(valores_climaticos.text)

url_valores = valores_json["datos"]

valores = requests.request("GET", url_valores, headers=headers)

print(valores.text)
