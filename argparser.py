import argparse

def bicimad(e: str):
    dest = input("Introduzca lugar de origen: ")
    print(args.e)
    print(f"ha elegido: {dest}")

def bicipark(e: str):
    print(args.e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Bienvenido a la app de Bicimad")
    parser.add_argument("-e", type=str, help='Introduce si quieres utilizar bicimad o bicipark')
    args = parser.parse_args()

    print(args.e)
    print(type(args))


    if args.e == 'bicimad':
        bicimad(args.e)
    elif args.e == 'bicipark':
        bicipark(args.e)
    else:
        print('Ha introducido errores. Vuelva a comenzar.')