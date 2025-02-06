### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

quantidade = 12 # Poderia ter trocado aqui por input
preco = 320 # Poderia ter trocado aqui por input

if isinstance(quantidade,int) and isinstance(preco,int):

    if quantidade > 0 and preco > 0:
        print(f'Dados validos! Quantidade: {quantidade} Preço: {preco}')
    else:
        print(f'Dados invalidos! Quantidade: {quantidade} Preço: {preco}')
### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

temperatura = 300

if temperatura > 100:
    print('Alta')
elif temperatura  < 50:
    print('Normal')
elif temperatura < 50:
    print('Baixa')
else:
    print(f'Sensor com algum problema {temperatura}')

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == 'ERROR':
    print(f'Erro leia mensagem: {log["message"]}')

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = 35
email = "guilherme@test.com"

if idade > 18 and idade < 65 and "@" in email:
    print(f'Dados de usuário válidos: idade: {idade} email: {email}')
else:
    print(f'Dados de usuário inválidos: idade: {idade} email: {email}')

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacao = {'valor': 12000, 'hora': 20}

if transacao['valor'] > 10000 or transacao['hora'] <9 or transacao['hora']>20:
    print('Transação suspeita!')
    if transacao['valor'] > 10000:
        print(f'Valor: {transacao["valor"]}')
    else:
        print(f'Horario: {transacao["hora"]}')
else:
    print("transação normal")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "Olá Mundo!"
contagem = {}
for palavra in texto:
    contagem[palavra] = contagem.get(palavra, 0) + 1

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)
normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

print(usuarios_validos)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

lista = [1,4,5,2,5,6,7,8,0,10,22]

for item in lista:
    if item % 2 == 0:
        print(f'É numero par: {item}')

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    ("Eletrônicos", 1500),
    ("Roupas", 300),
    ("Eletrônicos", 800),
    ("Alimentos", 200),
    ("Roupas", 450),
    ("Alimentos", 100),
    ("Eletrônicos", 1200),
]
total_vendas_por_categoria = {}

for categoria, valor in vendas:
    if categoria in total_vendas_por_categoria:
        total_vendas_por_categoria[categoria] += valor
    else:
        total_vendas_por_categoria[categoria] = valor

for categoria, total in total_vendas_por_categoria.items():
    print(f'Categoria: {categoria}, Total de Vendas: {total}')

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

while True:
    resposta = input("Digite algo. \nCaso queira encerrar digite sair:\n")

    if resposta == 'sair':
        break

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

while True:
    resposta = int(input("Digite algo. \nCaso queira encerrar digite um numero par > 12:\n"))

    if resposta % 2 == 0 and resposta > 12:
        break
    else:
        print('Bora digitar mais!')


### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

pagina_atual = 1
paginas_totais = 5  # Simulação, na prática, isso viria da API

while pagina_atual <= paginas_totais:
    print(f"Processando página {pagina_atual} de {paginas_totais}")
    # Aqui iria o código para processar os dados da página
    pagina_atual += 1

print("Todas as páginas foram processadas.")


### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

tentativas_maximas = 5
tentativa = 1

while tentativa <= tentativas_maximas:
    print(f"Numero de tentativa {tentativa} de {tentativas_maximas}")
    if True: 
        print("Conexão bem-sucedida!")
        break

    tentativa += 1
else:
    print("Falha ao conectar após várias tentativas.")

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

itens = [1,32,4,0,'Guilherme',0]

while True:

    if "Guilherme" in itens:
        print(f'Achei o valor alvo, encerrando...')
        break