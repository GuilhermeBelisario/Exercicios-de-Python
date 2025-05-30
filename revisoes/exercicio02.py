# Exercício 2: Processamento de Dados com `*args` e Operações em Sets

# - Objetivo: Praticar o uso de `*args` e operações com `set`.
    
# - Tarefa:
    
#     1. Crie uma função chamada `analisar_listas_numericas` que aceite um 
#         número indefinido de listas como argumentos posicionais (`*args`).
#     2. Dentro da função:
#         - Para cada lista recebida, converta-a para um `set` para remover duplicatas.
#         - Calcule e retorne um dicionário com as seguintes informações:
#             - `"uniao_total"`: Um `set` contendo a união de todos os elementos 
#                         únicos de todas as listas.
#             - `"intersecao_total"`: Um `set` contendo a interseção dos elementos 
#                         que aparecem em _todas_ as listas (se nenhuma lista for passada, 
#                       ou se a interseção for vazia, pode retornar um set vazio).
#             - `"elementos_unicos_por_lista"`: Uma lista de sets, onde cada set 
#                         contém os elementos únicos da lista original correspondente.

def analisar_listas_numericas(*args):
    if not args:
        return {
            "uniao_total": set(),
            "intersecao_total": set(),
            "elementos_unicos_por_lista": []
        }

    elementos_unicos_por_lista = [set(lista) for lista in args]

    uniao_total = set()
    for s in elementos_unicos_por_lista:
        uniao_total.update(s)

    intersecao_total = elementos_unicos_por_lista[0].copy() 
    for i in range(1, len(elementos_unicos_por_lista)):
        intersecao_total.intersection_update(elementos_unicos_por_lista[i])

    return {
        "uniao_total": uniao_total,
        "intersecao_total": intersecao_total,
        "elementos_unicos_por_lista": elementos_unicos_por_lista
    }

lista1 = [1, 2, 3, 4, 4, 5]
lista2 = [4, 5, 5, 6, 7, 8]
lista3 = [5, 8, 9, 10]

analise = analisar_listas_numericas(lista1, lista2, lista3)
print(f"Análise das listas: {analise}")

analise_com_duas_listas = analisar_listas_numericas([1, 2, 3], [3, 4, 5])
print(f"Análise com duas listas: {analise_com_duas_listas}")

analise_vazia = analisar_listas_numericas()
print(f"Análise sem listas: {analise_vazia}")