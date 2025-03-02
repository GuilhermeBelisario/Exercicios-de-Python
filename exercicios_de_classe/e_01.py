#Recursividade em Orientação a Objetos

#1. Fatorial Recursivo: Crie uma classe `Calculadora` com um método recursivo para calcular o fatorial de um número.

class Calculadora:
    def fatorial(self, num: int) -> int:
        if num < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if num == 0 or num == 1:
            return 1
        return num * self.fatorial(num - 1)

calculadora = Calculadora()
numero = int(input('Digite um numero: '))
resultado = calculadora.fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")

#2. Fibonacci Recursivo: Implemente uma classe`Fibonacci`com um método recursivo para calcular o n-ésimo termo da sequência de Fibonacci.

class Fibonacci:
    def calc_fibonacci(self, numero: int) -> int:
        if numero < 0:
            raise ValueError("n deve ser um inteiro não negativo.")
        if numero == 0:
            return 0
        if numero == 1:
            return 1
        return self.calc_fibonacci(numero - 1) + self.calc_fibonacci(numero - 2)

n = int(input("Digite um número para Fibonacci: "))
fibonacci_calc = Fibonacci()
resultado = fibonacci_calc.calc_fibonacci(n)
print(f"O {n}-ésimo termo da sequência de Fibonacci é {resultado}")


#3. Torre de Hanoi: Crie uma classe `TorreDeHanoi` que resolve o problema da Torre de Hanoi usando recursão.
class TorreDeHanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos

    def mover_discos(self, n, origem, destino, auxiliar):
        if n == 1:
            print(f"Mover disco {n} de {origem} para {destino}")
            return
        self.mover_discos(n - 1, origem, auxiliar, destino)
        
        print(f"Mover disco {n} de {origem} para {destino}")
        
        self.mover_discos(n - 1, auxiliar, destino, origem)

    def resolver(self):
        self.mover_discos(self.num_discos, 'A', 'C', 'B')

if __name__ == "__main__":
    num_discos = 3  
    hanoi = TorreDeHanoi(num_discos)
    hanoi.resolver()
