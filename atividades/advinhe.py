import random
numero_gerado= random.randint (1,20)

numero_digitado = 0
while numero_digitado != numero_gerado:
    numero_digitado= int(input("Advinhe o numero que eu pensei: "))
    if numero_digitado < numero_gerado:
        print("Muito baixo, tente denovo !")
    elif numero_digitado > numero_gerado:
        print("Muito alto, tente novamente!")
    else:
        print("Voce acertou, Muito bem!")
        break