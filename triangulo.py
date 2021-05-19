def calculate_area(b, h):
    return (b*h)/2;

def get_tringle_type(a, b, c):
    #TODO verify if triangle is valid
    if a==b and a==c:
        return "Equilatero"
    elif a!=b and a!=c:
        return "Escaleno"
    else:
        return "Isosceles"

def main() :
    print("Bienvenido a tringulos.py")
    base = float(input("Ingresa la base de tu triangulo (b): "))
    altura = float(input("Ingresa la altura de tu triangulo (h): "))
    area_triangulo = calculate_area(base, altura)
    print("El área de tu triangulo es: "+str(area_triangulo))
    lado_a = float(input("Ingresa la longitud del lado A: "))
    lado_b = float(input("Ingresa la longitud del lado B: "))
    lado_c = float(input("Ingresa la longitud del lado C: "))
    tipo_triangulo = get_tringle_type(lado_a, lado_b, lado_c)
    print("Tu triangulo es: "+ tipo_triangulo)

if __name__ == '__main__':
    main()
    