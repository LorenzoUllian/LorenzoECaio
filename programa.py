from funcoes import define_posicoes, preenche_frota, posicao_valida #importamos do arquivo funcoes.py

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

# nome: [tamanho, quantidade]
navios = {
    "porta-aviões": [4, 1],
    "navio-tanque": [3, 2],
    "contratorpedeiro": [2, 3],
    "submarino": [1, 4],
}

for nome in navios:
    tamanho = navios[nome][0]
    quantidade = navios[nome][1]

    i = 0
    while i < quantidade:
        valida = False
        while not valida:
            print("Insira as informações referentes ao navio", nome, "que possui tamanho", tamanho)
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if nome == "submarino":
                orientacao = "horizontal"
            else:
                opcao = int(input("[1] Vertical [2] Horizontal >"))
                if opcao == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"

            valida = posicao_valida(frota, linha, coluna, orientacao, tamanho)
            if not valida:
                print("Esta posição não está válida!")

        frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
        i += 1

print(frota)

from funcoes import *

frota = {}

navios = [
    ['porta-aviões', 4, 1],
    ['navio-tanque', 3, 2],
    ['contratorpedeiro', 2, 3],
    ['submarino', 1, 4],
]

for navio in navios:
    nome = navio[0]
    tamanho = navio[1]
    quantidade = navio[2]
    for i in range(quantidade):
        valido = False
        while not valido:
            print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            orientacao = 'horizontal'
            if nome != 'submarino':
                escolha = int(input('Orientação: [1] Vertical [2] Horizontal '))
                if escolha == 1:
                    orientacao = 'vertical'
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valido = True
            else:
                print('Esta posição não está válida!')

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

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

ataques = []
jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    repetida = True
    while repetida:
        linha = int(input('Jogador, qual linha deseja atacar? '))
        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Jogador, qual linha deseja atacar? '))

        coluna = int(input('Jogador, qual coluna deseja atacar? '))
        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Jogador, qual coluna deseja atacar? '))

        if [linha, coluna] in ataques:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        else:
            repetida = False

    ataques.append([linha, coluna])
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False


