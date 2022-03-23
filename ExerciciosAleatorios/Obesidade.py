# ======================================================================
#                           Medida De Obesidade
# ======================================================================

altura_ok = False
tipo_altura_ok = False
while not (altura_ok and tipo_altura_ok):
    try:
        altura = float(input("Digite sua altura em [m]: "))
        tipo_altura_ok = True
        if altura <= 0: 
            print("ERRO: A altura deve ser um número real positivo")
        else:
            altura_ok = True
    except ValueError:
        print("ERRO: A altura deve ser um número real positivo")
massa_ok = False
tipo_altura_ok = False
while not (massa_ok and tipo_altura_ok):
    try:
        massa = float(input("Digite sua massa em [kg]: "))
        tipo_altura_ok = True
        if altura <= 0: 
            print("ERRO: A massa deve ser um número real positivo")
        else:
            massa_ok = True
    except ValueError:
        print("ERRO: A massa deve ser um número real positivo")
IMC = massa / altura ** 2

if IMC < 18.5:
    classificacao = "Abaixo do peso"
elif IMC < 25:
    classificacao = "Saudável"
elif IMC < 30:
    classificacao = "Peso em excesso"
elif IMC < 35: 
    classificacao = "Obesidade grau 1"
elif IMC < 40: 
    classificacao = "Obesidade grau 2 (severa)"
else:
    classificacao = "Obesidade grau 3 (mórbida)"
print(f'Seu IMC vale {IMC:.2f}')
print(f'classificacção: {classificacao}')