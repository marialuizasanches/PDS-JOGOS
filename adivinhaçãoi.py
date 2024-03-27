import random

numeroSecreto = random.randint(1, 101)
tentativas = 0


def jogar():
   
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")
   
    NivelDificuldade()
   
    print("numero secreto", numeroSecreto)
    global tentativas
    while tentativas > 0:
        numeroDigitado = int(
            input("Digite um número de 1 a 100 para tentar advinhar o número secreto:"))
        if numeroDigitado == numeroSecreto:
            print("Parabéns o número escolhido está correto")
            print("O número secreto era", numeroSecreto)
            break
        else:
            tentativas -= 1
            print("O número digitado está errado")
            print(dica(numeroDigitado))
            if tentativas > 0:
                print("Tente novamente, você tem:", tentativas, "tentativas")
            else:
                print("Game Over")


def dica(numeroEscolhido: int):
    print("Escolhido", numeroEscolhido, "Secreto", numeroSecreto)
    if numeroEscolhido > numeroSecreto:
        return "O número escolhido é maior que o número secreto,", numeroEscolhido
    else:
        return "O numero escolhido é menor que o número secreto", numeroEscolhido
       
def NivelDificuldade():
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    dificuldade = int(input("Defina o nível:"))
    global tentativas
    if (dificuldade == 1):
        tentativas = 10
    elif (dificuldade == 2):
        tentativas = 8
    else:
        tentativas = 6
       
jogar()
