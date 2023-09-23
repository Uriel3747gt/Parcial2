#Elabore un programa de linea de comandos para calcular areas de multiples figuras el cual debe recibir como primer argumento el tipo de figura a calcular y luego un conjunto de datos para calcular el area, los valores de cada figura
#estan separados por comas y cada figura por |.
import argparse
import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def main():
    parser = argparse.ArgumentParser(description='Calcula áreas de figuras geométricas')
    parser.add_argument('figura', choices=['circulo', 'rectangulo', 'triangulo'], help='Tipo de figura (circulo, rectangulo o triangulo)')
    parser.add_argument('datos', help='Datos de la figura separados por comas. Por ejemplo, para un círculo: radio; para un rectángulo: base,altura; para un triángulo: base,altura')

    args = parser.parse_args()

    datos = [float(x) for x in args.datos.split(',')]

    if args.figura == 'circulo' and len(datos) == 1:
        area = calcular_area_circulo(datos[0])
        print(f'Área del círculo con radio {datos[0]} es {area:.2f}')
    elif args.figura == 'rectangulo' and len(datos) == 2:
        area = calcular_area_rectangulo(datos[0], datos[1])
        print(f'Área del rectángulo con base {datos[0]} y altura {datos[1]} es {area:.2f}')
    elif args.figura == 'triangulo' and len(datos) == 2:
        area = calcular_area_triangulo(datos[0], datos[1])
        print(f'Área del triángulo con base {datos[0]} y altura {datos[1]} es {area:.2f}')
    else:
        print('Error: Revise los argumentos proporcionados.')

if __name__ == "__main__":
    main()
