################# Menú en consola ##################
#Estrada Cabrera Nadia Abigali

from blessed import Terminal 
from Figuras import Cuadrado, Rectangulo, Circulo, Triangulo 
    
term = Terminal()

def Menu():
    print (("______________________________________________________________________________________"))
    print (term.bold_purple("BIENVENIDO A ESTE PROGRAMA PARA EL CÁLCULO DE PERÍMETRO Y ÁREA DE FIGURAS GEOMETRICAS"))
    print (("______________________________________________________________________________________"))
    print (term.bold_purple("Elige la figura que quieras calcular:"))
    print (term.blue("1. Rectangulo"))
    print (term.blue("2. Cuadrado"))
    print (term.blue("3. Circulo"))
    print (term.blue("4. Triángulo"))
    print (term.red("5. Salir"))
    opcion = input("Seleccione una opcion: ")
    return opcion

def main():
    
    while True:
        opcion = Menu()

        if opcion == "1":
            
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            print(cuadrado)
            print(term.green("Calculando perimetro y área del RECTANGULO"))
            print(f"Area: {cuadrado.area()}")
            print(f"Perimetro: {cuadrado.perimetro()}")

        elif opcion == "2":

            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            rectangulo = Rectangulo(base, altura)
            print(rectangulo)
            print(term.green("Calculando perimetro y área del CUADRADO"))
            print(f"Area: {rectangulo.area()}")
            print(f"Perimetro: {rectangulo.perimetro()}")

        elif opcion == "3":

            radio = float(input("Ingrese el radio del circulo: "))
            circulo = Circulo(radio)
            print(circulo)
            print(term.green("Calculando perimetro y área del CIRCULO"))
            print(f"Area: {circulo.area()}")
            print(f"Perimetro: {circulo.perimetro()}")

        elif opcion == "4":

            base = float(input("Ingrese la base del triangulo: "))
            altura = float(input("Ingrese la altura del triangulo: "))
            ladoiz = float(input("Ingrese el lado izquierdo del triangulo: "))
            ladode = float(input("Ingrese el lado derecho del triangulo: "))

            triangulo = Triangulo(base, altura, ladoiz, ladode)
            print(triangulo)
            print(term.green("Calculando perimetro y área del TRIANGULO"))
            print(f"Area: {triangulo.area()}")
            print(f"Perimetro: {triangulo.perimetro()}")

        elif opcion == "5":

            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida, intente de nuevo.")
            
if __name__ == "__main__":
    main()