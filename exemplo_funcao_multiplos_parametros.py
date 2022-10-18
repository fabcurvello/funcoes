"""
Podemos utilizar um recurso bastante facilitador ao criar funções que podem receber muitos parâmetros:
"""

# Exemplo inicial, sem utilizar o recurso de múltiplos parâmetros em funções
def somar(n1, n2, n3):
    total = n1 + n2 + n3
    return total


print(somar(1,1,1))

nums = [2, 3, 4]
print(somar(*nums)) # O * faz o unpacking do list nums, passando cada parâmetro para n1, n2 e n3

 # ----

# Exemplo utilizando o recurso de múltiplos parâmetros em funções
def somar_multiplos_parametros(*numeros): # O * faz o packing dos parâmetros recebidos no list numeros
    total = 0
    for numero in numeros:
        total += numero
    return total


print(somar_multiplos_parametros(1,1,1))
print(somar_multiplos_parametros(1,1,1,1,1,1,1))
