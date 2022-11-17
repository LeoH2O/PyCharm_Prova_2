# Lista dado [ 1,2,3,4,5,6]
import random
dado = [1, 2, 3, 4, 5, 6]
jogador_1 = []
jogador_2 = []

print("Jogar - 1")
print("Sair - 2")
soma_player1 = 0
soma_player2 = 0
menu = (int(input("Escolha: Jogar/Sair: ")))
while True:
    if menu == 1:
        jogador1 = random.choice(dado)
        jogador_1.append(jogador1)
        jogador2 = random.choice(dado)
        jogador_2.append(jogador2)
        print(f'O Jogador 1 tirou o valor {jogador1}')
        print(f'O Jogador 2 tirou o valor {jogador2}')
        soma_player1 += jogador1
        soma_player2 += jogador2
        play_again = int(input("Escolha: 1-Jogar/ 2-Sair: "))

        if play_again != 1:
            print(f'Jogadas do Jogador 1: {jogador_1}')
            print(f'Jogadas do Jogador 2: {jogador_2}')
            print(f'Soma dos valores do Jogador 1: {soma_player1}')
            print(f'Soma dos valores do Jogador 2: {soma_player2}')
            if soma_player1 == soma_player2:
                print("Empate")
                print("Obrigado por jogar!")
            elif soma_player1 > soma_player2:
                print("Jogador 1 é o vencedor")
                print("Obrigado por jogar!")
            else:
                print("Jogador 2 é o vencedor")
                print("Obrigado por jogar!")
            break
