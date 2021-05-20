import math

def area_cilindro():
    radio = float(input("Ingrese el radio del cilindro: "))
    altura = float(input("Ingrese la altura del cilindro: "))
    area = math.pi*(radio**2)*altura
    print("El área del cilindro es: "+str(area))

def area_cubo():
    lado = float(input("Ingrese la longitud de un lado del cubo: "))
    area = lado**3;
    print("El área del cubo es: "+str(area))

def area_esfera():
    radio = float(input("Ingrese el radio de la esfera: "))
    area = (4/3)*math.pi*(radio**3);
    print("El área de la esfera es: "+str(area))

def area_ortoedro():
    base = float(input("Ingrese la longitud de la base: "))
    altura = float(input("Ingrese la longitud de la altura: "))
    profundidad = float(input("Ingrese la longitud de la profundidad: "))
    area = base*altura*profundidad;
    print("El área del ortoedro es: "+str(area))

def area_cono():
    radio = float(input("Ingrese el radio del cono: "))
    altura = float(input("Ingrese la altura del cono: "))
    area = (math.pi*(radio**2)*altura)/3
    print("El área del cono es: "+str(area))

def main():
    print("Bienvenido a calculadora de volumenes")
    seleccion = 0
    while seleccion!=6:
        print("----MENU----")
        print("1. Area de un cilindro")
        print("2. Area de un cubo")
        print("3. Area de un esfera")
        print("4. Area de un ortoedro")
        print("5. Area de un cono")
        print("6. Salir")
        seleccion = int(input("Seleccion: "))
        if(seleccion==1):
            area_cilindro()
        elif(seleccion==2):
            area_cubo()
        elif(seleccion==3):
            area_esfera()
        elif(seleccion==4):
            area_ortoedro()
        elif(seleccion==5):
            area_cono()
        elif(seleccion!=6):
            print("Seleccion invalida")

if __name__ == '__main__':
    main()
    