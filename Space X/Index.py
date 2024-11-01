import requests
import pandas as pd
import numpy as np
import datetime
#parece que el import, como en java, se bugea, hay que reiniciar el vs code

# esto pinta todas las columnas del df
pd.set_option("display.max_columns", None)
# pinta toda la data en una feature
pd.set_option("display.max_colwidth",None)


# pilla el dataset y usa la columna de cohete para llamar a la API y añadir los datos a la lista
def getBoosterVersion(data):
    for x in data['rocket']:
        if x:
            response = requests.get("https://api.spacexdata.com/v4/rockets/"+str(x)).json()
            BoosterVersion.append(response['name'])


# Toma el conjunto de datos y usa la columna launchpad para llamar a la API y agregar los datos a la lista
def getLaunchSite(data):
    for x in data['launchpad']:
        if x:
            response = requests.get("https://api.spacexdata.com/v4/payloads/"+load).json()
            PayloadMass.append(response['logitude'])
            Latitude.append(response['latitude'])
            LaunchSite.append(response['name'])


# Toma el conjunto de datos y usa la columna launchpad para llamar a la API y agregar los datos a la lista
def getPayloadData(data):
    for load in data['payloads']:
        if load:
            response = requests.get("https://api.spacexdata.com/v4/payloads/"+load).json()
            PayloadMass.append(response['mass_kg'])
            Orbit.append(response['orbit'])
            
            
def getCoreData(data):
    for core in data[data] != None:
        if core['core'] != None:
                response = requests.get("https://api.spacexdata.com/v4/cores/"+core['core']).json()
                Block.append(response['block'])
                ReusedCount.append(response['reuse_count'])
                Serial.append(response['serial'])
        else:
                Block.append(None)
                ReusedCount.append(None)
                Serial.append(None)
            Outcome.append(str(core['landing_success'])+' '+str(core['landing_type']))
            Flights.append(core['flight'])
            GridFins.append(core['gridfins'])
            Reused.append(core['reused'])
            Legs.append(core['legs'])
            LandingPad.append(core['landpad'])
            
# ahora empezamos a llamar con la url
spacex_url="https://api.spacexdata.com/v4/launches/past"
response = requests.get(spacex_url)
print(response.content)

#hay que usar un metodo statico para la consistencia de este resultado del json
static_json_url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/API_call_spacex_api.json'

#Si viene con un 200 es que esta ok
response.status_code
