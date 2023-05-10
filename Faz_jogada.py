#Define Posições
def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_f=[]
    if orientacao == 'horizontal':
        for i in range (0,tamanho):
            lista_f.append([linha, coluna +i])
    elif orientacao =='vertical':
        for i in range (0,tamanho):
            lista_f.append([linha +i, coluna])
    return lista_f

#Preenche Frota
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    if nome_navio in frota:
        frota[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))
    else:
        frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    return frota

#Faz Jogada
def faz_jogada(tabuleiro, linha, coluna):
    marca = 'X' if tabuleiro[linha][coluna] == 1 else '-'
    tabuleiro[linha][coluna] = marca
    return tabuleiro