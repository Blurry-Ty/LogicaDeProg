intervalo = int(input('Intervalo de tempo em segundos: '))

horas = intervalo // 3600
minutos = intervalo % 3600//60
segundos = intervalo % 3600 % 60

print(f'''O intervalo de tempo é de {horas} horas {minutos} minutos {segundos} segundos''')