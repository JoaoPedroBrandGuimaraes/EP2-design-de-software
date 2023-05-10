#Define Posições
def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_f=[]
    if orientacao == 2:
        for i in range (0,tamanho):
            lista_f.append([linha, coluna +i])
    elif orientacao ==1:
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

#Posiciona Frota
def posiciona_frota(dicionario_informacoes):
    tabuleiro = [[0 for j in range(10)] for i in range(10)]
    for navio, posicoes in dicionario_informacoes.items():
        for posicionamento in posicoes:
            for linha, coluna in posicionamento:
                tabuleiro[linha][coluna] = 1
    return tabuleiro

#Quantas Embarcações Afundadas?
def afundados(dicionario, tabuleiro):
    navios_afundados = 0
    for navio in dicionario.values():
        for posicoes in navio:
            if all(tabuleiro[linha][coluna] == 'X' for linha, coluna in posicoes):
                navios_afundados += 1
    return navios_afundados

#Posição Válida
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicionamentos = define_posicoes(linha, coluna, orientacao, tamanho)
    for navio in frota.values():
        for posicao_navio in navio:
            if any(posicao in posicao_navio for posicao in posicionamentos):
                return False
    return all(0 <= posicao[0] < 10 and 0 <= posicao[1] < 10 for posicao in posicionamentos)

#Posicionando Frota
frotas={}
tamanhos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
tipos = ['porta-aviões', 'navio-tanque', 'navio-tanque', 'contratorpedeiro', 
         'contratorpedeiro', 'contratorpedeiro', 'submarino', 'submarino', 
         'submarino', 'submarino']

for i, tamanho in enumerate(tamanhos):
    tipo = tipos[i]
    valido = False
    while not valido:
        print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(tipo, tamanho))
        linha = int(input('Linha:'))
        coluna = int(input('Coluna:'))
        orientacao = int(input('[1] Vertical [2] Horizontal >'))
        valido = posicao_valida(frotas, linha, coluna, orientacao, tamanho)
        if not valido:
            print('Esta posição não está válida!')
    frotas = preenche_frota(frotas, tipo, linha, coluna, orientacao, tamanho)