#gerar o número aleatório#
import random


def jogar_adivinhacao(): #função q guarda o código#
    numero_secreto = random.randint(1, 100) #faz com q o número seja de 1 ao 100#
    tentativas = 0 #define que o número de tentativas inicial seja 0 para a contagem de tentativas#

    print("=====================================")
    print("Bem-vindo ao jogo de Adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")
    print("Tente adivinhar!")
    print("=====================================")


    while True: #loop infinito até que o participante acerte o número ou desista#
        tentativa = input("Digite um número (ou 'desistir' para sair): ")

        if tentativa.lower() == 'desistir':#solicita que o participante digite um número ou desistir#
            print("=====================================")
            print(f"O número secreto era: {numero_secreto}")
            print("Desistiu do jogo. Melhor sorte da próxima vez!")
            print("=====================================")
            break

        tentativa = int(tentativa)
        tentativas += 1 #cálculo do número de tentativas#

        if tentativa == numero_secreto:#verifica se o número digitado é igual ao pensado#
            print("=====================================")
            print(f"Parabéns! Você acertou em {tentativas} tentativa(s)!")
            print("=====================================")
            break
        elif tentativa < numero_secreto:#caso seja um número maior#
            print("Tente um número maior!")
        else:#caso seja um número menor#
            print("Tente um número menor!")

    print("Obrigado por jogar!")

jogar_adivinhacao() #chama a função pra iniciar o jogo#
