import random
Esq = input("Digite (S) para soma e (M) para multiplicação: ")

n1 = random.randint(0, 100)
n2 = random.randint(0, 100)


def teste():
    if Esq.casefold() == "s":
        print ("Esses são os numeros somados N1 = " + n1 + "N2 = " + n2)
        print (n1 + n2)
    elif Esq.casefold() == "m":
        print ("Esses são os numeros multiplicados N1 = " + n1 + "N2 = " + n2)
        print (n1 * n2)

if Esq.casefold() != "s" or Esq.casefold() != "m": 
    print ("Escolha novamente")
    teste()
    

teste()