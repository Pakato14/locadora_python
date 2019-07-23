def palavras():

    palavras = []
    qtd_palavras = int(input('Digite a quantidade de palavras que deseja usar no jogo: '))

    while len(palavras) <= qtd_palavras:
        palavra = input('Digite a palavra secreta: ')
        palavras.append(palavra)
        arquivo = open('palavras.txt', 'w')
        for palavras_secretas in palavras:
            arquivo.writelines(palavras_secretas + '\n')
        arquivo.close()

    print('Palavras salvas com sucesso!')
