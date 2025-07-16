lista_dict = [
    {"usuario": "Kenzo", "paginas": 18},
    {"usuario": "Matheus", "paginas": 39},
    {"usuario": "Beto", "paginas": 99}
]

def verificadora_leitura(lista, quantidade_min_pag = 30):
    lista_nomes_grandes_leitores = []
    
    
    for dicionario in lista:
        itens_do_dict = [] 
        for itens in dicionario.values():
            itens_do_dict.append(itens)
        if itens_do_dict[1] > quantidade_min_pag:
            lista_nomes_grandes_leitores.append(itens_do_dict[0])
    return lista_nomes_grandes_leitores

print(f"O nome do(s) usuário(s) que superam o limite mínimo de páginas lidas pré-estabelecidos é de: {verificadora_leitura(lista_dict)}")