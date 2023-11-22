##############################################################################
#                                                                            #                       
#   argparse — Parser for command-line options, arguments and sub-commands   #     
#                                                                            #
#   Ironhack Data Part Time --> Sep-2023                                    #
#                                                                            #
##############################################################################


# import library
import pandas as pd
import argparse

from modules.bicimad import saludo


def elegir(categoria, sitio):

    bicimad_df =  pd.read_csv('./resultados/resultados_bicimad.csv')
    bicipark_df = pd.read_csv('./resultados/resultados_bicipark.csv')

    print(f'Has elegido: {categoria}\n')
    
    if sitio == None:
        pass
    else:
        print(f'En el lugar: {sitio}')
    


    if categoria == 'Bicimad':

        if sitio == None:
            print(bicimad_df)

        else:
            print(f'El bicimad más cercano es: {bicimad_df[bicimad_df["title"]==sitio]["address_bicimad"].iloc[0]} ')
            print(f'En esta distancia: {bicimad_df[bicimad_df["title"]==sitio]["distancia"].iloc[0]} metros')
        



    if categoria == 'Bicipark':

        if sitio == None:
            print(bicipark_df)

        else:
            print(f'El Bicipark más cercano es: {bicipark_df[bicipark_df["title"]==sitio]["name_bicipark"].iloc[0]}')
            print(f'En esta distancia: {bicipark_df[bicipark_df["title"]==sitio]["distancia"].iloc[0]} metros')
        
    else:
        print('Ha introducido errores. Vuelva a comenzar.')





# Argument parser function
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= "Bienvenido a la app de Bicimad" )

    parser.add_argument('-e', help = 'Selecciona Bicimad Bicipark', type=str)
    parser.add_argument('-s', help= 'Sitio de interes', type=str)

    saludo()

    args = parser.parse_args()
    elegir(args.e, args.s)