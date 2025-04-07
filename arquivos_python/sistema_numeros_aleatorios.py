import random

# Função principal do jogo de adivinhação
def jogo_adivinhaçao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número entre 1 e 100. Tente adivinhar!")

    # O computador escolhe um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    # Loop até o usuário acertar o número
    while acertou == False:
        # O usuário tenta adivinhar
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        # Verifica se o palpite é o correto
        if palpite < numero_secreto:
            print("Seu palpite esta muito baixo. Tente novamente!")
        elif palpite > numero_secreto:
            print("Seu palpite está muito alto. Tente novamente!")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
            acertou = True  # O jogo termina quando o número é acertado

# Chama a função para começar o jogo
jogo_adivinhação()