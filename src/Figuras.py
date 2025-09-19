################# Programa: Cálculo de perímetro y área ##################
#Estrada Cabrera Nadia Abigali
    
class Cuadrado:
    
    #Crear constructor
    def __init__ (self, lado: float):
        self.lado = lado
        
    #PERIMETRO  
    def perimetro(self):
            return self.lado*self.lado
        
    #AREA
    def area(self):
         return self.lado*self.lado
     
class Rectangulo:
    
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    #PERIMETRO
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    #AREA
    def area(self):
        return self.base * self.altura
    
    
    def __str__(self):
        return f"Rectangulo de base {self.base} y altura {self.altura}"

class Circulo:
    
    
    def __init__(self, radio):
        self.radio = radio
    
    #PERIMETRO
    def perimetro(self):
        return 2 * 3.1416 * self.radio
    
    #AREA
    def area(self):
        return 3.1416 * (self.radio ** 2)
    
    def __str__(self):
        return f"Circulo de radio {self.radio}"

class Triangulo:
    
    
    def __init__(self, base, altura, lado1, lado2):
        self.base = base
        self.altura = altura
        self.lado_1 = lado1
        self.lado_2 = lado2
        
    
    #PERIMETRO
    def perimetro(self):
        return self.base + self.lado_1 + self.lado_2
    
    #AREA
    def area(self):
        return (self.base * self.altura) / 2
    
    def __str__(self):
        return f"Triangulo de base {self.base} y altura {self.altura}"