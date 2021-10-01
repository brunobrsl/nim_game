def computador_escolhe_jogada(n, m):
    qtd = n % (m + 1)

    if qtd > 0:
        return qtd
    return m

def usuario_escolhe_jogada(n, m):
    jogada = 0

    while jogada == 0:
        jogada = int(input("Quantas peças você vai tirar? "))
        print()

        if jogada > n or jogada < 1 or jogada > m:
            jogada = 0
            print("Oops! Jogada inválida! Tente de novo.\n")
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()

    while (n < m or n < 1 or m < 1):
            print("Oops! A quantidade inserida é inválida! Tente novamente.\n")
            n = int(input("Quantas peças? "))
            m = int(input("Limite de peças por jogada? "))
            print()

    vez_computador = True

    if n % (m + 1) == 0:
        vez_computador = False

    if (vez_computador == True):
        print("Computador começa!")
        print()
    else:
        print("Voce começa!")
        print()

    while n > 0:
        if vez_computador:
            jogada = computador_escolhe_jogada(n, m)
            vez_computador = False
            if(jogada == 1):
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", jogada, "peças.")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            vez_computador = True
            if(jogada == 1):
                print("Você tirou uma peça.")
            else:
                print("Você tirou", jogada,"peças.")
        n = n - jogada
        if(n == 1):
            print("Agora resta apenas uma peça no tabuleiro.\n")
        else:
            if(n > 1):
                print("Agora restam", n,"peças no tabuleiro.\n")

    if vez_computador:
        print("Fim do jogo! Você ganhou!")
    
    else:
        print("Fim do jogo! O computador ganhou!")

def campeonato():
    pt_comp = 0
    pt_usuario = 0
    i = 1
    while (i <= 3):
        print("\n**** Rodada", i, "****\n")
        vencedor = partida()
        if (vencedor == 1):
            pt_usuario = pt_usuario + 1
        else: 
            pt_comp = pt_comp + 1
        i = i + 1
    print("\n**** Final do campeonato! ****\n")
    print("Placar: Você", pt_usuario, "X", pt_comp,"Computador")



def main(): 
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    selecao = int(input("2 - para jogar um campeonato "))

    while (selecao < 1 or selecao > 2):
        print("\nOpção inválida!\n")
        print("1 - para jogar uma partida isolada")
        selecao = int(input("2 - para jogar um campeonato "))
    
    if(selecao == 1):
        print("\nVoce escolheu partida única!\n")
        partida()
    else:
        print("\nVoce escolheu um campeonato!")
        campeonato()

main()