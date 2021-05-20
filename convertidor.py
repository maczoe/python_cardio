

def convert_km_to_miles(km):
    return km * 0.621371

def convert_miles_to_km(miles):
    return miles * 1.609344;

def main():
    print("Bienvenido a convertidor.py")
    seleccion = 0;
    while seleccion!=3:
        print("----MENU----")
        print("1. Millas a kilometros")
        print("2. Kilometros a millas")
        print("3. Salir")
        seleccion = int(input("seleccion: "))
        if(seleccion==1):
            miles = float(input("Ingrese la cantidad en millas: "))
            print(str(miles) + " milla(s) equivale a "+ str(convert_miles_to_km(miles)) + " Kms")
        elif(seleccion==2):
            km = float(input("Ingrese la cantidad en kilometros: "))
            print(str(km) + " kilometro(s) equivale a "+ str(convert_km_to_miles(km)) + " millas")
        elif(seleccion!=3):
            print("Opcion invalida")

if __name__ == '__main__':
    main()
    