#Dicionario
dic = {'Nome':'João', 'Idade' :'30'}

#Pegando apenas uma parte do dicionario
print(dic['Idade'])

Formatar = 24.00000

#Formatar 2 casas decimais / Funciona com Str
print(f'{Formatar:.2f}' )

#Formata casa decimais, arredonda não funciona com Str
print(round(Formatar, 2))