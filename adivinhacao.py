import random

def jogar_adivinhacao():

    print('*'*35)
    print('******* Jogo de adivinhação *******')
    print('*'*35)

    numero = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("Níveis do jogo")
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input(('Defina o nível: ')))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    elif(nivel == 3):
        tentativas = 5

    for rodada in range(1, tentativas+1):
        print('Tentativa {} de {}'.format(rodada, tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print('Você digitou: ',chute)

        if(chute < 1 or chute > 100):
            print('Vocẽ deve digitar um número entre 1 e 100.')
            continue

        acertou = numero == chute
        maior = numero < chute
        menor = numero > chute


        if(acertou):
            print('Parabéns! Se garantiu, acertou!!')
            print('O número secreto é {} e sua pontuação foi {} '.format(numero, pontos))
            break
        else:
            if(maior):
                print('Você digitou um número maior do que o prêmiado!')
                pontos_perdidos = abs(chute - numero)
                pontos = pontos - pontos_perdidos
                if(rodada == tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero, pontos))

            elif(menor):
                print('Você digitou um número menor do que o prêmiado!')
                pontos_perdidos = abs(chute - numero)
                pontos = pontos - pontos_perdidos
                if (rodada == tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero, pontos))

    print('Fim do Jogo!')

if(__name__ == '__main__'):
    jogar_adivinhacao()