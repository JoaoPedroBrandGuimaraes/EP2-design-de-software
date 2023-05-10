def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_f=[]
    if orientacao == 'horizontal':
        for i in range (0,tamanho):
            lista_f.append([linha, coluna +i])
    elif orientacao =='vertical':
        for i in range (0,tamanho):
            lista_f.append([linha +i, coluna])
    return lista_f
  
def preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho):
    if nome_navio not in frota.keys():
        frota[nome_navio] = []
    frota[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))
    return frota
    
def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna]==1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(dicionario_informacoes):
    tabuleiro=[]
    for i in range(0,10):
        lista2=[]
        for j in range (0,10):
            lista2.append(0)
        tabuleiro.append(lista2)

    for posicoes in dicionario_informacoes.values():
        for posicionamento in posicoes:
            for posicao_precisa in posicionamento:
                tabuleiro[posicao_precisa[0]][posicao_precisa[1]] = 1
    return tabuleiro

def afundados(dicionario,tabuleiro):
    navios_afundados=0
    for navios in dicionario.values():
        for navio_especifico in navios:
            valor=0
            for coordenada in navio_especifico:
                linha = coordenada[0]
                coluna = coordenada[1]
                if tabuleiro[linha][coluna] == 'X':
                    valor +=1
                    if valor == len(navio_especifico):
                        navios_afundados +=1
    return navios_afundados

def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_f=[]
    if orientacao == 2:
        for i in range (0,tamanho):
            lista_f.append([linha, coluna +i])
    elif orientacao ==1:
        for i in range (0,tamanho):
            lista_f.append([linha +i, coluna])
    return lista_f


def posicao_valida(frota,linha,coluna,orientacao,tamanho):
    posicionamentos = define_posicoes(linha,coluna,orientacao,tamanho)
    for navios in frota.values():
        for navio_especifico in navios:
            for posicao_exata in posicionamentos:
                if posicao_exata in navio_especifico:
                    return False
    for posicao_exata in posicionamentos:
        indice1 = posicao_exata[0] < 0
        indice2 = posicao_exata[0] >=10
        indice3 = posicao_exata[1] <0
        indice4 = posicao_exata[1] >=10

        if indice1 or indice2 or indice3 or indice4:
            return False
    return True