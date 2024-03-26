
def jogar():
  print("***MARIA LUIZA SANCHES***")
palavra_secreta = "maluzinha".upper()
letras_acertadas = ["-" for letra in palavra_secreta]
letras_acertadas2 = []
for letra in (palavra_secreta):
  letras_acertadas2.append("-")
enforcou = False
acertou = False
erros = 0
print(letras_acertadas)
while(not enforcou and not acertou):
  chute = input("Qual letra? ")
  chute = chute.strip().upper()
  if(chute in palavra_secreta):
    index = 0
    for letra in palavra_secreta:
      if (chute == letra):
        letras_acertadas[index] = letra
      index += 1
  else:
    erros += 1
  enforcou = erros == 6
  acertou = "-" not in letras_acertadas
  print(letras_acertadas)
if(acertou):
  print("Voce ganhou!")
else:
  print("Voce perdeu!")
print("Fim do jogo")
if (__name__ == "__main__"):
  jogar()
