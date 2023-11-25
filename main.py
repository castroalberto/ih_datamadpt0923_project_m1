
# import library
import pandas as pd
import argparse
from modules.bicimad import update_bicimad
from modules.bicipark import update_bicipark



def elegir(categoria, sitio):

    bicimad_df =  pd.read_csv('./resultados/resultados_bicimad.csv')
    bicipark_df = pd.read_csv('./resultados/resultados_bicipark.csv')

    
    
    if sitio == None:
        pass
    else:
        print(f'Has elegido: {categoria}\n')
        print(f'En el lugar: {sitio}')
    


    if categoria == 'Bicimad':

        if sitio == None:
            print(bicimad_df)

        else:
            print(f'El Bicimad más cercano es: {bicimad_df[bicimad_df["title"]==sitio]["address_bicimad"].iloc[0]} ')
            print(f'En esta distancia: {bicimad_df[bicimad_df["title"]==sitio]["distancia"].iloc[0]} metros\n')
        



    elif categoria == 'Bicipark':

        if sitio == None:
            print(bicipark_df)

        else:
            print(f'El Bicipark más cercano es: {bicipark_df[bicipark_df["title"]==sitio]["name_bicipark"].iloc[0]}')
            print(f'En esta distancia: {bicipark_df[bicipark_df["title"]==sitio]["distancia"].iloc[0]} metros\n')





# Argument parser function
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= "Bienvenido a la app de Bicimad" )
    parser.add_argument('-e', help = 'Selecciona Bicimad Bicipark para conocer el listado de estaciones más cercanas a cada punto de interes', type=str)
    parser.add_argument('-s', help= 'Añada su lugar de interes para conocer la el Bicimad o Bipark mas cercano a este punto' , type=str)
    parser.add_argument('-u', help= 'Seleccione Bicimad o Bicipark para actualizar la base de datos' , type=str)


    args = parser.parse_args()
    elegir(args.e, args.s)
    update_bicimad(args.u)
    update_bicipark(args.u)