import pandas as pd
import requests as re
from geopy.distance import geodesic


def update_bicimad(update):

    if update == 'Bicimad':

        #LEEMOS NUESTRO FICHERO BICIMAD
        bicimad_df = pd.read_csv('./data/bicimad_stations.csv', sep = '\t')

        #EXTRAEMOS LAS COORDENADAS DE BICIMAD, NOS QUEDAMOS CON EL DIGITO Y LAS AGREGAMOS A UNA COLUMNA
        bicimad_df['longitude'] = bicimad_df.apply(lambda row: row[
            'geometry.coordinates'].replace("[","").replace("]","").split(', ')[0], 
                                                axis=1)
        bicimad_df['latitude'] = bicimad_df.apply(lambda row: row[
            'geometry.coordinates'].replace("[","").replace("]","").split(', ')[1], 
                                                axis=1)

        bicimad_clean = bicimad_df[['id','name','address','longitude','latitude']]


        #CONECTAMOS CON LA WEB PARA OBTENER JSON
        base_url = "https://datos.madrid.es/egob"
        body = "/catalogo/209434-0-templos-otros.json"
        response = re.get(base_url + body)
        print(response)

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




        #CREACION DE UN DATAFRAME CON LA DISTANCIAS MINIMAS DE CADA TEMPLO A NUESTRO BICIMAD o PARK

        # Agregar nuevas columnas a templos_clean para almacenar datos de la fila en bicimad_clean
        templos_clean['distancia'] = float('inf')
        templos_clean['name_bicimad'] = ""
        templos_clean['address_bicimad'] = ""

        # iteramos sobre cada linea del dataframe de TEMPLOS
        for index_templo, templo in templos_clean.iterrows():
            
            #variables donde guardaremos los datos de la fila ganadora en bicimad_clean que seran columnas del df final
            min_distance = float('inf')
            name_ganador = ""
            address_ganadora = ""

            #recorre el dataframe bicimad calculando la distancia una a una del templo en el que está el for superior
            for index_bicimad, bicimad in bicimad_clean.iterrows():
                
                coordenadas_templo = (templo['latitude'], templo['longitude'])
                coordenadas_bicimad = (bicimad['latitude'], bicimad['longitude'])
                #calculamos la distancia con geodesic en cada caso
                distancia = geodesic(coordenadas_templo, coordenadas_bicimad).meters
            
                #solo actualiza si esta distancia es menor a la que ya tiene, asegurando la menor.
                if distancia <= min_distance:
                    min_distance = distancia
                    name_ganador = bicimad['name']
                    address_ganadora = bicimad['address']

            # Actualizar las columnas en templos_clean con la información de la fila ganadora
            templos_clean.at[index_templo, 'distancia'] = min_distance
            templos_clean.at[index_templo, 'name_bicimad'] = name_ganador
            templos_clean.at[index_templo, 'address_bicimad'] = address_ganadora

        templos_con_distancias = templos_clean.copy()
        templos_con_distancias.to_csv('./resultados/resultados_bicimad.csv', index=False)

        print('')
        print('********** ARCHIVO BICIMAD ACTUALIZADO *********')
    else:
        pass


