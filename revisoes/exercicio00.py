#Revisão de conceitos basicos!

# Exercicio 1

class Carro:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_dados(self):
        print(f'A marca é {self.marca} e o modelo é {self.modelo}')
    
fiat_uno = Carro('Fiat','Uno')
meu_carro = Carro("Volkswagen", "Gol")

fiat_uno.mostrar_dados()
meu_carro.mostrar_dados()

# Exercicio 2

class Circulo:
    
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = 3.14159 * (self.raio * self.raio)
        return area
    

circulo1 = Circulo(10)
area_circulo1 = circulo1.calcular_area()
print(f"A área do círculo é: {area_circulo1}")
    