valores = []

for i in range(0,3):
    val = int(input("Digite seu Valor: "))
    valores.append(val)

res = (valores[0] + valores[1] ) * valores[2]

print(res)