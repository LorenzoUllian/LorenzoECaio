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
