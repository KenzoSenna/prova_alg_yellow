from functools import reduce
turma_a = [
    ("Kenzo", 8),
    ("Hudson", 10),
    ("Abner", 9)
]
turma_b = [
    ("Richard", 7),
    ("Pedro", 4),
    ("Teo", 7)
]
dicionario_lista_tuplas = [
    {"turma_a": turma_a},
    {"turma_b": turma_b}
]

def media_geral_turmas(nomes_turmas, *args):
    contador = -1
    resultado = {}
    for contador in range(len(args)):
        contador += 1
        for turma in args[contador]:
            lista_notas = []
            for aluno in turma:
                lista_notas.append(aluno[1])
            media = reduce(lambda x, y: x + y, lista_notas) / len(lista_notas)
            for dicionario in nomes_turmas:
                for nomes in dicionario.keys():
                    nome_turma = nomes
                    if nome_turma:
                        resultado[nome_turma] = media 
        return resultado
print(media_geral_turmas(dicionario_lista_tuplas, turma_a, turma_b))