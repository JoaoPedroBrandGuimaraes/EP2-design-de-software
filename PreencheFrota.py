def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_f=[]
    if orientacao == 2:
        for i in range (0,tamanho):
            lista_f.append([linha, coluna +i])
    elif orientacao ==1:
        for i in range (0,tamanho):
            lista_f.append([linha +i, coluna])
    return lista_f
  
def preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho):
    if nome_navio not in frota.keys():
        frota[nome_navio] = []
    frota[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))
    return frota