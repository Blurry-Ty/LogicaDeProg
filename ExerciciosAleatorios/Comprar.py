# preco1 = int(input("Digite o preço do item 1: "))
# preco2 = int(input("Digite o preço do item 2: "))
# preco3 = int(input("Digite o preço do item 3: "))

# subtotal = preco1 + preco2 + preco3

# print(subtotal)

# total = subtotal * 1.07

# print(total)

TAXA = 0.07

Num_itens = int(input("Digite o numero de itens desejados: "))

itens = []

for item in range(Num_itens):
    preco = float(input(f'Valor do item #{item+1}:'))
    itens.append(preco)
subtotal = sum(itens)

print (subtotal)
print (subtotal * TAXA)
print (subtotal + subtotal * TAXA)