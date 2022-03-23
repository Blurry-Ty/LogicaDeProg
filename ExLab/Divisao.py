
import os 
import math
os.system('cls') or None

import time
Escolha = int(input("Escolha o que deseja: \n1 - Para descobrir todos os divisores do valor \n2 - Para descobrir todos os primos de 0 até o valor desejado\n"))

def achar_divisores(valor):
    list = []
    inicio = time.time()
    for i in range(1, int(valor**0.5) +1 ):
        if valor % i == 0:
            list.append (i)
            if valor // i != i:
                list.append (valor//i)
    list.sort()
    fim = time.time()
    tempo = fim - inicio
    
    return list, tempo
    

tempos, primos = [], [1]
def achar_primos(valor):
    for a in range(1 , valor + 1):
        list, tempo = achar_divisores(a)

        if len(list) == 2:
            primos.append(a)
        tempos.append(tempo) 
    print (primos)

if Escolha == 1:
    valor = int(input("Digite um valor: "))
    achar_divisores(valor)
    list, tempo = achar_divisores(valor)
    print (f'\n{list}')
    print (f'\nO tempo para o processamento dos divisores foi de {tempo:.4}\n')
    
elif Escolha == 2:
    valor = int(input("Digite um valor: "))
    achar_primos(valor)
else:
    print("Erro escolha uma das opcoes disponiveis")