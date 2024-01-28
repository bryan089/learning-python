#api_nasa.py
#API: Aplication programming interface --> consumo de datos vamos a trabajar
#Nasa API: Get comets https://api.nasa.gov/
#API_KEY_NASA: YuIvzIDww0zeddsFdJ0goouGJxcHXeKY7DTpXl3P
#Developer: Brayan Solarte
#Date: 24012024
#https://pypi.org/project/requests/
'''Get and read data from NASA API about comets'''

import requests
import os

os.system('clear')

def get_comet_data(api_key):
	print("::: COMMET INFORMATION :::\n")
	url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"
	

	try:
		#realizar la solicitud a la API
		response = requests.get(url)
		response.raise_for_status()# Valida si se presenta algun error en la peticion
		#convertir la respuesta a formato JSON (JS object Notation)
		datos = response.json()

		print(f"Comet name: {datos['name']}")
		print(f"Absolute magnitude: {datos['absolute_magnitude_h']}")
		print(f"Estimated diameter max (KM): {datos['estimated_diameter']['kilometers']['estimated_diameter_max']}")
		print(f"Estimated diameter max (FT): {datos['estimated_diameter']['feet']['estimated_diameter_max']}")
	

	except requests.exceptions.RequestException as e:
		print(f"Error al realizar la peticion a la API de NASA: {e}")
	

api_key_nasa = "YuIvzIDww0zeddsFdJ0goouGJxcHXeKY7DTpXl3P"
get_comet_data(api_key_nasa)	
