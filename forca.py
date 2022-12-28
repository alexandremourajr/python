import random


def jogar():
    mensagemBoasVindas()
    palavra_secreta = geraPalavraSecreta()

    enforcou = False
    acertou = False
    erros = 0

    letras_acertadas = inicializaLetrasAcertadas(palavra_secreta)



    while (not enforcou and not acertou):
        print(letras_acertadas, '\n')
        chute = pedeChute()

        if (chute in palavra_secreta):
            verificaChute(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)


        enforcou = erros == 7
        acertou = "_" not in letras_acertadas


    if (acertou):
        mensagemVencedor()
    else:
        mensagemPerdedor(palavra_secreta)


def mensagemBoasVindas():
    print("********************************")
    print("   Bem vindo ao Jogo de Forca   ")
    print("********************************\n")


def geraPalavraSecreta():
    with open("palavras.txt") as arquivo:
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip().upper())

    palavra_secreta = palavras[random.randrange(0, len(palavras))]
    return palavra_secreta

def inicializaLetrasAcertadas(palavra_secreta):
   letras_acertadas = ["_" for letra in palavra_secreta]
   return letras_acertadas

def pedeChute():
    chute = input("Digite uma Letra: ").strip().upper()
    return chute

def verificaChute(palavra_secreta,chute,letras_acertadas):
    index = 0
    for letra in palavra_secreta:

        if (chute == letra):
            letras_acertadas[index] = letra

        index += 1

def mensagemVencedor():
    print("Você ganhou")

def mensagemPerdedor(palavra_secreta):

    print("Você perdeu")
    print("A palavra secreta era: ",palavra_secreta)


def desenha_forca(erros):

    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()

