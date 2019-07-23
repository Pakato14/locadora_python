import adivinhacao
import forca
import palavras

print('*'*35)
print('******** Locadora do Cobra ********')
print('*'*35)

print('Escolha seu jogo')
print('(1) Jogo da Adivinhação (2) Jogo da Forca (3) Salvar palavras para o jogo da Forca')

jogo = int(input('Defina o Jogo que quer jogar: '))

if(jogo == 1):
    print('Jogando Adivinhação')
    adivinhacao.jogar_adivinhacao()
elif(jogo == 2):
    print('Jogando Forca')
    forca.jogar_forca()
elif(jogo == 3):
    print('Salvar palavras')
    palavras.palavras()
