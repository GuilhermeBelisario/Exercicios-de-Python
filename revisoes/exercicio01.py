# **Exercício 1: Filtragem com Lambda e Sets**

# - **Objetivo:** Praticar `lambda` e `set` para processamento de dados.
    
# - **Tarefa:**
    
#     1. Crie uma lista de dicionários, onde cada dicionário representa 
# um produto com as chaves "nome" (string), "preco" (float) e "categoria" (string).
        
#         Python
        
#         ```
#         produtos = [
#             {"nome": "Laptop", "preco": 3500.00, "categoria": "Eletrônicos"},
#             {"nome": "Mouse", "preco": 80.00, "categoria": "Eletrônicos"},
#             {"nome": "Cadeira Gamer", "preco": 1200.00, "categoria": "Móveis"},
#             {"nome": "Teclado", "preco": 150.00, "categoria": "Eletrônicos"},
#             {"nome": "Mesa Digitalizadora", "preco": 450.00, "categoria": "Eletrônicos"},
#             {"nome": "Monitor", "preco": 900.00, "categoria": "Eletrônicos"},
#             {"nome": "Luminária de Mesa", "preco": 60.00, "categoria": "Móveis"},
#         ]
#         ```
        
#     2. Escreva uma função chamada `filtrar_produtos_caros_por_categoria` 
# que receba a lista de produtos e um valor `preco_minimo`.
#     3. Dentro desta função, use `filter()` com uma função `lambda` para 
# selecionar apenas os produtos cujo preço seja maior ou igual ao `preco_minimo`.
#     4. A partir dos produtos filtrados, retorne um `set` 
# contendo apenas os nomes das _categorias_ desses produtos caros (para evitar duplicatas de categorias).


produtos = [
    {"nome": "Laptop", "preco": 3500.00, "categoria": "Eletrônicos"},
    {"nome": "Mouse", "preco": 80.00, "categoria": "Eletrônicos"},
    {"nome": "Cadeira Gamer", "preco": 1200.00, "categoria": "Móveis"},
    {"nome": "Teclado", "preco": 150.00, "categoria": "Eletrônicos"},
    {"nome": "Mesa Digitalizadora", "preco": 450.00, "categoria": "Eletrônicos"},
    {"nome": "Monitor", "preco": 900.00, "categoria": "Eletrônicos"},
    {"nome": "Luminária de Mesa", "preco": 60.00, "categoria": "Móveis"},
]

def filtrar_produtos_caros_por_categoria(lista_produtos, preco_minimo):

    produtos_filtrados = filter(lambda produto: produto["preco"] >= preco_minimo, lista_produtos)

    
    categorias_caras = set()
    for produto in produtos_filtrados:
        categorias_caras.add(produto["categoria"])

    return categorias_caras

preco_limite = 500.00
categorias_de_produtos_caros = filtrar_produtos_caros_por_categoria(produtos, preco_limite)
print(f"Categorias com produtos acima de R${preco_limite:.2f}: {categorias_de_produtos_caros}")

preco_limite_2 = 1000.00
categorias_de_produtos_muito_caros = filtrar_produtos_caros_por_categoria(produtos, preco_limite_2)
print(f"Categorias com produtos acima de R${preco_limite_2:.2f}: {categorias_de_produtos_muito_caros}")