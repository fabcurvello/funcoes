"""
Função filter realiza um filtro em uma lista, onde cada item verificado só pode dar verdadeiro ou falso.
Esta função retorna uma nova lista contendo somente os itens qye ao serem testados deram verdadeiro.
"""

lista_idade = [5, 15, 37, 19, 8, 47, 22, 13, 77]

lista_maior_de_idade = filter( lambda idade: idade >= 18, lista_idade )

print(list(lista_maior_de_idade)) # Resposta: [37, 19, 47, 22, 77]

print(list(lista_maior_de_idade)) # Resposta: [] ???

for idade in lista_maior_de_idade:
    print(idade)  # Resposta: - NADA - ???

