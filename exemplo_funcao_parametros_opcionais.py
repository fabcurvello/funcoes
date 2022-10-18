def calcular_media( nota1, nota2, ponto_extra=0 ):
    md = ((nota1 + nota2) / 2) + ponto_extra
    return md


def situacao_aluno(nota1, nota2, ponto_extra=0, nome=""):
    media = calcular_media(nota1, nota2, ponto_extra)

    if (media >= 7):
        sit = "APROVADO(A)"
    else:
        sit = "REPROVADO(A)"


    if (nome == ""):
        print(f"Média: {media}, Situação: {sit}")
    else:
        print(f"Média do(a) aluno(a) {nome}: {media}, Situação: {sit}")


#print(calcular_media(7, 8))
#print(calcular_media(7, 8, 1))

print(situacao_aluno(7, 8))
#print(situacao_aluno(7, 8, 1))
#print(situacao_aluno(9, 9, 1, "Fabricio"))
#print(situacao_aluno(7,8, nome="Alberto"))
#print(situacao_aluno(3,4, ponto_extra=1, nome="Carla"))