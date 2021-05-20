
def main():
    print("Bienvenido a rangos_cambiantes.py")
    inferior = float(input("Ingresa el limite inferior: "))
    superior = float('-inf')
    while inferior>=superior:
        superior = float(input("Ingresa el limite superior: "))
        if inferior>=superior:
            print("Limite superior invalido")

    bandera = True
    while bandera:
        valor = float(input("Ingresa un valor a comparar: "))
        print("Tu valor es: " + str(valor))
        if valor>=inferior and valor<=superior:
            print("Tu valor esta dentro del limite")
            bandera = False
        else:
            print("Tu valor esta fuera del limite")

if __name__ == '__main__':
    main()
    