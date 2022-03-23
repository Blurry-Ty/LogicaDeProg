import os
os.system('cls') or None


# Inputs
print ("*** Raiz Quadrada Aproximada ***")
radicando = float(input("Extrair a raiz quadrada de: "))
casas_dec = int(input("Qual a precisão desejada (casas decimais)? "))


# Variaveis

precisao = 10**(-casas_dec)
tentativas = 0
low = 0
high = radicando
raiz = (low + high)/2

while (abs(raiz**2-radicando) >= precisao):
    tentativas +=1
    if raiz**2 < radicando:
        low = raiz  
    else: 
        high = raiz
    raiz = (low + high)/2


print (f'''\nA raiz quadrada de {radicando} é {raiz:.{casas_dec}f} dentro da precisão de {precisao}.\nForam necessarias {tentativas} tentativas. ''')
