import random
print('**************************')
print('Bem vindo ao jogo de forca')
print('**************************')

palavras = ["maça", "banana", "melao", "melancia", "carro", "tomate", "televisao"]

numero = random.randrange(0, len(palavras))

palavra_secreta = palavras[numero].upper()
letras_acertadas = ["_"for letra in palavra_secreta]

enforcou = False
acertou = False
erros = 0

print(letras_acertadas)

while (not enforcou and not acertou):

  chute = input("Qual letra? ")
  chute = chute.strip().upper()

  if (chute in palavra_secreta):
    index = 0
    for letra in palavra_secreta:
      if (chute == letra):
          letras_acertadas[index] = letra
      index += 1
  else:
    erros += 1
    
  enforcou = erros == 6 
  acertou = "_" not in letras_acertadas
  print(letras_acertadas)

if (acertou):
    print("Parabéns, você ganhou!")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ") 
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
if (enforcou):
    print("Puxa, você foi enforcado!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

print('Fim do Jogo')