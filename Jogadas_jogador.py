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

#Jogadas do Jogador
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
frota_jogador = frotas

tabuleiro_oponente = posiciona_frota(frota_oponente)

tabuleiro_jogador = posiciona_frota(frota_jogador)

jogando = True

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto


posicoes_atacadas = []

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    linha_ataque = int(input('Jogador, qual linha deseja atacar?'))
    coluna_ataque = int(input('Jogador, qual coluna deseja atacar?'))

    if linha_ataque < 0 or linha_ataque > 9 or coluna_ataque < 0 or coluna_ataque > 9:
        print('Coordenadas inválidas!')
        continue

    posicao_ataque = [linha_ataque, coluna_ataque]
    if posicao_ataque in posicoes_atacadas:
        print('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha_ataque, coluna_ataque))
        continue

    posicoes_atacadas.append(posicao_ataque)
    tabuleiro = faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)
    n_afundados = afundados(frota_oponente, tabuleiro_oponente)

    if n_afundados == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

