lista_pacientes = [
    ("Roberto", 1),
    ("José", 4),
    ("Kenzo", 3)
]

def mais_tres_sessoes(lista):
    lista_dos_mais_ativos = []

    for paciente in lista:
        if paciente[1] > 3:
            lista_dos_mais_ativos.append(paciente[0])
    return lista_dos_mais_ativos

print(f"O(s) paciente(s) que possuem mais de 3 agendamentos é(são): {mais_tres_sessoes(lista_pacientes)}")