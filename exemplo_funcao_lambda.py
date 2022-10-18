"""
Função LAMBDA (ou expressão Lambda) é um tipo de função que não possui nome definido.
Também pode ser chamado de função anônima
"""

# exemplo de uma função tradicional
def somar(n1, n2):
    return n1 + n2


print(somar(2,3))

# exemplo de função LAMBDA
soma = lambda n1, n2: n1 + n2
print(soma(3,4))