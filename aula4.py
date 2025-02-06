
#Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

lista = []

for i in range(1,11):
    lista.append(i)

new_lista = [print(i ** 2) for i in lista]

#Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

lista =  ["Python", "Java", "C++", "JavaScript"]
lista.remove('C++')
lista.append("Ruby")

print(lista)
#Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

livros = {}

titulo = input('Passe o titulo: ')
autor = input('Quem escreveu? ')
ano = int(input("Ano de publicação: "))

if isinstance(ano,int):
    livros['Titulo'] = titulo
    livros['Autor'] = autor
    livros['Ano'] = ano
    print(livros)
else:
    print("Verifique o ano digitado!")

#Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

texto = "Sovita Mais Energia para Vida"

dicionario = {'texto': texto}
contador = {}

for caractere in dicionario['texto']:
    if caractere in contador:
        contador[caractere] += 1
    else:
        contador[caractere] = 1

print(contador)


#Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(precos[item] for item in lista_compras)
print(f"Preço total: {total}")


#Exercícios de Funções

#Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

def soma_lista(lista):
    resultado = sum(lista)
    return resultado

lista = [1,34,2,3,4,65]
resposta = soma_lista(lista)
print(resposta)

#Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

def numero_e_primo(numero):
    if numero <= 1:
        return False  
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False 
    return True 

numero = 3
if numero_e_primo(numero):
    print(f'O número {numero} é primo')
else:
    print(f'O número {numero} não é primo')

#Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

def reverte_string(palavra):
    palavra_invertida = palavra[:: -1]
    return palavra_invertida

palavra = 'dsnvosdofij'
print(reverte_string(palavra))

#Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.

def somador(lista,numero):
    nova_lista = []
    nova_lista.append([x + numero for x in lista])

    return nova_lista

lista = [1,2,3,4,6]
numero = 2

somador(lista,numero)

#Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas

def ordenador_de_chaves_de_dicionarios(dicionario):
    
    chaves_ordenadas = sorted(dicionario.keys())
    return chaves_ordenadas


teste = {'ProdutoA': 20, 'ProdutoB': 10, 'ProdutoC': 30}
resultado = ordenador_de_chaves_de_dicionarios(teste)
print(resultado)