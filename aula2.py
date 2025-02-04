# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num1 = int(input("Digita um numero"))
num2 = int(input("Digita outro numero"))

if isinstance(num1,int) and isinstance(num2, int):
    num3 = num1 + num2
    print(num3)
else:
    print('Verifique os valores digitados e tente novamente')

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num1 = int(input("Digita um numero"))
num2 = int(input("Digita outro numero"))

if isinstance(num1,int) and isinstance(num2, int):
    num3 = num1 % num2
    print(num3)
else:
    print('Verifique os valores digitados e tente novamente')

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
num1 = int(input("Digita um numero"))
num2 = int(input("Digita outro numero"))
if isinstance(num1,int) and isinstance(num2, int):
    num3 = num1 * num2
    print(num3)
else:
    print('Verifique os valores digitados e tente novamente')
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num1 = int(input("Digita um numero"))
num2 = int(input("Digita outro numero"))

if isinstance(num1,int) and isinstance(num2,int):
    num3 = num1 / num2 
    print(num3)
else:
    print('Verifique os valores digitados e tente novamente')
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

num1 = int(input("Digita um numero"))
num2 = int(input("Digita outro numero"))

if isinstance(num1,int) and isinstance(num2,int):
    num3 = num1 ** num2
    print(num3)

else:
    print('Verifique os valores digitados e tente novamente.')

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
num1 = float(input("Digita um numero"))
num2 = float(input("Digita outro numero"))

if isinstance(num1, float) and isinstance(num2,float):
    num3 = num1 + num2
    print(num3)
else:
    print('Verifique os valores digitados')

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

num1 = float(input("Digita um numero"))
num2 = float(input("Digita outro numero"))

if isinstance(num1,float) and isinstance(num2,float):
    num3 = (num1 + num2) / 2
    print(f'Média é {num3}')

else:
    print('Verifique os valores digitados')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

num1 = int(input("Digita um numero para base"))
num2 = int(input("Digita outro numero para o expoente"))

if isinstance(num1,int) and isinstance(num2,int):
    num3 = num1 ** num2
    print(f'Base: {num1} Expoente: {num2} Resultado: {num3}')
else:
    print('Verifique os valores digitados')

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

celsius = 25
Fahrenheit  = (celsius * 1.8) + 32

print(f'Temperatura em celsius: {celsius} Temperatura em fahrenheit: {Fahrenheit}')

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import numpy as np

pi = np.pi
raio = 5

area_do_circulo = pi * (raio ** 2)
print(f'Considerando {pi} Raio: {raio} Area do Ciculo = {area_do_circulo}')

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

texto = input("Escreve um texto: ")
print(texto.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

texto = "Guilherme Belisario"
print(texto.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no iníio e no final.

frase = input("Digite uma frase: ")
print(frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input("Escreva uma data no formado dd/mm/aa: ")
data_list = data.split('/')

print(f'A data digitada foi: {data} sendo dia {data_list[0]} mes {data_list[1]}  ano {data_list[2]}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

frase1 = input("Digite uma frase: ")
frase2 = input("Digite uma frase: ")

frase_concatenada = frase1 + frase2

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

entrada1 = input("Digite o primeiro valor booleano (True ou False): ").strip().capitalize()
entrada2 = input("Digite o segundo valor booleano (True ou False): ").strip().capitalize()

bool1 = entrada1 == "True"
bool2 = entrada2 == "True"

resultado = bool1 and bool2

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

entrada1 = input("Digite True ou False: ").strip().capitalize()
entrada2 = input("Digite True ou False: ").strip().capitalize()

bool1 = entrada1 == "True"
bool2 = entrada2 == "True"

resultado = bool1 or bool2
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

entrada = input("Digite True ou False: ").strip().capitalize()

valor_trocado = not entrada

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

num1 = int(input("Digita um numero"))
num2 = int(input("Digita outro numero"))
if num1 == num2:
    print("Os números são iguais.")
else:
    print("Os números são diferentes.")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura

temperatura = input("Qual a temperatura? (Apenas numeros)")

converter_para = input("""Digite para qual deseja converter:
                    1 C para F
                    2 F para C """)

if converter_para == 1:
    temperatura_convertida = (temperatura * 1.8) + 32
elif converter_para == 2:
    temperatura_convertida = (temperatura - 32) / (5/9)
else:
    print('Parece que houve um problema na digitação. Tente novamente.')

# 22: Verificador de Palíndromo
number = 4224

numero_inveritod = int(str(number[:: -1]))

if number == numero_inveritod:
    print('É Palindromo')
else:
    print('Não palimdromo')


# 23: Calculadora Simples

while True:

    resposta = int(input("""
                        
    Escolha qual operação vc quer fazer (Digitando o numero correspondente):)
        1. Soma
        2. Subtração
        3. Divisão
        4. Multiplicação
        
                        
    """))

    if resposta is not None:

        if resposta == "5":
            print("Encerrando!")
            break
            
        try:

            num1 = int(input("Primeiro numero: "))
            num2 = int(input("Segundo numero: "))
            
            if resposta == 1:
                print(num1 + num2)
                
            elif resposta == 2:
                print(num1 - num2)
                

            elif resposta == 3:
                print(num1 / num2)
                

            elif resposta == 4:
                print(num1 * num2)

            else:
                print("Verifique o numero digitado!")

        except Exception as e:
            print(f'Ocorreu algum problema: {e}')
    else:
        print('Parece que você não escolheu corretamente a operação!')

# 24: Classificador de Números

num1 = 20  
num2 = 3 
resultado_divisao_inteira = num1 // num2
print("O resultado da divisão inteira é:", resultado_divisao_inteira)

# 25: Conversão de Tipo com Validação

numero = 2
print(type(str(numero)))