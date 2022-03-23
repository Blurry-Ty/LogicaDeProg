print("1 - À vista (PIX, Dinheiro ou Cheque): 10"+ "%" + " de desconto")
print("2 - À vista (Crédito): 5" + "%" + "de desconto")
print("3 - 2 parcelas (Crédito): sem desconto")
print("4 - 3 ou mais parcelas(Crédito): juros de 20%")
Esq = int(input("Escolha uma das opções acima: "))
preco = float(input("Quanto custa o produto? "))
if Esq == 1:
    print(preco * 0.9)
elif Esq == 2:
    print(preco * 0.95)
elif Esq == 3:
    print(preco/2)
elif Esq == 4:
    quant_parc = int(input("Escolha até 3 parcelas: "))
    pre = preco * 1.2
    print (pre/ quant_parc)
else:
    print("ERROR")