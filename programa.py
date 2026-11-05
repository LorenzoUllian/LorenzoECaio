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


