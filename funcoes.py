def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    i = 0
    while i < tamanho:
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
        i += 1
    return posicoes


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = []
    frota[nome_navio].append(posicoes)
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro


def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        linha_tab = []
        for j in range(10):
            linha_tab.append(0)
        tabuleiro.append(linha_tab)

    for navio in frota:
        for lista_posicoes in frota[navio]:
            for posicao in lista_posicoes:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro


def afundados(frota, tabuleiro):
    contador_afundados = 0

    for navio in frota:
        for lista_posicoes in frota[navio]:
            navio_afundado = True

            for posicao in lista_posicoes:
                linha = posicao[0]
                coluna = posicao[1]

                if tabuleiro[linha][coluna] != 'X':
                    navio_afundado = False
                    break

            if navio_afundado:
                contador_afundados += 1

    return contador_afundados



def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    novas_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in novas_posicoes:
        l = posicao[0]
        c = posicao[1]
        if l < 0 or l > 9 or c < 0 or c > 9:
            return False

    for navio in frota:
        for lista_posicoes in frota[navio]:
            for pos_existente in lista_posicoes:
                for nova_pos in novas_posicoes:
                    if pos_existente == nova_pos:
                        return False
    return True

def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    i = 0
    while i < tamanho:
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
        i += 1
    return posicoes


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]
    return frota


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicoes:
        
        if posicao[0] < 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 9:
            return False
        
        for nome in frota:
            for navio in frota[nome]:
                if posicao in navio:
                    return False
    return True

def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    i = 0
    while i < tamanho:
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
        i += 1
    return posicoes


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]
    return frota


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro


def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        linha_tab = []
        for j in range(10):
            linha_tab.append(0)
        tabuleiro.append(linha_tab)
    for navio in frota:
        for lista_posicoes in frota[navio]:
            for posicao in lista_posicoes:
                tabuleiro[posicao[0]][posicao[1]] = 1
    return tabuleiro


def afundados(frota, tabuleiro):
    contador_afundados = 0
    for navio in frota:
        for lista_posicoes in frota[navio]:
            navio_afundado = True
            for posicao in lista_posicoes:
                if tabuleiro[posicao[0]][posicao[1]] != 'X':
                    navio_afundado = False
                    break
            if navio_afundado:
                contador_afundados += 1
    return contador_afundados


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicoes:
        if posicao[0] < 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 9:
            return False
        for nome in frota:
            for navio in frota[nome]:
                if posicao in navio:
                    return False
    return True


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '___________________________________      ___________________________________\n'
    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto



