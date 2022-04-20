import requests
import json
import datetime


url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/"

querystring = {"api_key":"apikey_solicitada_a_aemet"} #pedir apikey en https://opendata.aemet.es/centrodedescargas/inicio

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

now = datetime.datetime.now()
date_time_sup = now.strftime("%Y-%m-%dT00:00:00UTC")
date_time_inf = (now - datetime.timedelta(days=7)).strftime("%Y-%m-%dT00:00:00UTC")
print(date_time_sup,date_time_inf)

#date_time_sup = "2020-03-02T00:00:00UTC"
#date_time_inf = "2020-02-26T00:00:00UTC"
#print(date_time_sup,date_time_inf)

url_valores_climaticos = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/" + date_time_inf + "/fechafin/" + date_time_sup + "/estacion/" + indicativo_log

valores_climaticos = requests.request("GET", url_valores_climaticos, headers=headers, params=querystring)

print(valores_climaticos.text)

valores_json=json.loads(valores_climaticos.text)

url_valores = valores_json["datos"]

valores = requests.request("GET", url_valores, headers=headers)

print(valores.text)
