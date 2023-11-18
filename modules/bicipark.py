import pandas as pd
import requests as re
from geopy.distance import geodesic

#LEEMOS NUESTRO FICHERO bicipark
bicipark_df = pd.read_csv('../data/bicipark_stations.csv', sep = ';')
#EXTRAEMOS LAS COORDENADAS DE bicipark, NOS QUEDAMOS CON EL DIGITO Y LAS AGREGAMOS A UNA COLUMNA
bicipark_df['longitude'] = bicipark_df.apply(lambda row: row[
    'geometry.coordinates'].replace("[","").replace("]","").split(', ')[0], 
                                           axis=1)
bicipark_df['latitude'] = bicipark_df.apply(lambda row: row[
    'geometry.coordinates'].replace("[","").replace("]","").split(', ')[1], 
                                          axis=1)

bicipark_clean = bicipark_df[['stationId','stationName','address','longitude','latitude']][:10]



#CONECTAMOS CON LA WEB PARA OBTENER JSON
base_url = "https://datos.madrid.es/egob"
body = "/catalogo/209434-0-templos-otros.json"
response = re.get(base_url + body)

#LEEMOS LOS TEMPLOS DEL JSON
content = response.content
json_data = response.json()
json_data.keys()

templos = pd.DataFrame(json_data['@graph'])

def separator_longitud_json(column): #devuelve valor como float64
    for i in column:
        return column["longitude"]
def separator_latitud_json(column): #devuelve valor como float64
    for i in column:
        return column["latitude"]
    
templos['longitude'] = templos.apply(lambda row: separator_longitud_json(row["location"]), axis=1)
templos['latitude'] = templos.apply(lambda row: separator_latitud_json(row["location"]), axis=1)   

templos_clean = templos[['id','title','longitude','latitude']]



#CREACION DE UN DATAFRAME CON LA DISTANCIAS MINIMAS DE CADA TEMPLO A NUESTRO bicipark o PARK

# Agregar nuevas columnas a templos_clean para almacenar datos de la fila en bicipark_clean
templos_clean['distancia'] = float('inf')
templos_clean['name_bicipark'] = ""
templos_clean['address_bicipark'] = ""

# iteramos sobre cada linea del dataframe de TEMPLOS
for index_templo, templo in templos_clean.iterrows():
    
    #variables donde guardaremos los datos de la fila ganadora en bicipark_clean que seran columnas del df final
    min_distance = float('inf')
    name_ganador = ""
    address_ganadora = ""

    #recorre el dataframe bicipark calculando la distancia una a una del templo en el que está el for superior
    for index_bicipark, bicipark in bicipark_clean.iterrows():
        
        coordenadas_templo = (templo['latitude'], templo['longitude'])
        coordenadas_bicipark = (bicipark['latitude'], bicipark['longitude'])
        #calculamos la distancia con geodesic en cada caso
        distancia = geodesic(coordenadas_templo, coordenadas_bicipark).meters
       
        #solo actualiza si esta distancia es menor a la que ya tiene, asegurando la menor.
        if distancia <= min_distance:
            min_distance = distancia
            name_ganador = bicipark['stationName']
            address_ganadora = bicipark['address']

    # Actualizar las columnas en templos_clean con la información de la fila ganadora
    templos_clean.at[index_templo, 'distancia'] = min_distance
    templos_clean.at[index_templo, 'name_bicipark'] = name_ganador
    templos_clean.at[index_templo, 'address_bicipark'] = address_ganadora

templos_con_distancias = templos_clean.copy()
templos_con_distancias.to_csv('../resultados/resultados_bicipark.csv', index=False)


