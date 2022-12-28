import random

def jogar():
    print("\n Bem vindo ao Jogo da Adivinhação")
    print("********************************\n")
    print("Qual o nível de dificuldade você gostaria de jogar?")
    print("1. Fácil - 15 Tentativas\n2. Médio - 10 Tentativas\n3. Díficil - 5 Tentativas\n")

    #INPUT DO USUÁRIO
    dificuldade = int(input())
    numero_secreto = random.randrange(0,101)
    pontos = 1000
    total_tentativas = 0

    # LOOP NÍVEL DE DIFICULDADE
    if (dificuldade == 1):
        total_tentativas = 15
    elif (dificuldade == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

        #LOOP INPUT - CHUTE USUÁRIO
    for tentativa in range(1,(total_tentativas+1)):
        print(f'Tentativa {tentativa} de {total_tentativas}')
        chute = int(input("Digite um número de 0 a 100: "))
        if (chute < 0 or chute > 100):
            print("Digite um número válido")
            continue

        # VARIÁVEIS
        acertou = chute == numero_secreto
        maior = chute > numero_secreto

        # LOOP PARA TESTAR O CHUTE
        if(acertou):
            print(f"Você acertou em {tentativa} tentativas\n")
            print("O seu total de pontos foi:{}".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto\n")

            else:
                print("Você errou! O seu chute foi menor que o número secreto\n")
            pontos_perdidos = abs(numero_secreto-chute)
            pontos -= pontos_perdidos


    print("Fim de jogo!")

if(__name__ =="__main__"):
    jogar()