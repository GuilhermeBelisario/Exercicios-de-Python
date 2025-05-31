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
    
# Exercicio 3 - Lambda

dobrar = lambda x: x * 2

print(dobrar(7))

# Exercicio 4

eh_par = lambda n: n % 2 == 0


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultados_paridade = list(map(eh_par, numeros))

print(f"Lista original: {numeros}")
print(f"Cada número é par? (True/False): {resultados_paridade}")

# Exercicio 5

lista = [1,2,5,6,7,10]

lista_nova = [ item * item for item in lista ]

print(lista_nova)

# Exercicio 6

palavras = ["oi", "Python", "sim", "não", "dados"]

lista = [item for item in palavras if len(item) > 3]

print(lista)

# Exercicios 7

pares = [item for item in range(11) if item % 2 ==0]

print(pares)