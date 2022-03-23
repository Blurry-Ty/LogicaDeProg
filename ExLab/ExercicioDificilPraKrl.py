'''
a, b, c = input().split()
d, e, f = input().split()

b = int(b)
c = float(c)
e = int(e)
f = float(f)

x = b*c + e*f
print("VALOR A PAGAR: R$ %.2f" % x)

import math

x1 ,y1 = input().split()
x2 ,y2 = input().split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

soma = math.sqrt(((x2-x1) * (x2-x1)) + ((y2-y1)*(y2-y1)))
print (f"{soma:.4f}")
'''
# -*- coding: utf-8 -*-

a = float(input())
teste = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
notas = []
x = a + 0.01

for c in teste:
    z = x//c
    x = x%c
    notas.append(z)

print (f'\nNotas:\n{notas[0]} nota(s) de R$ 100.00\n{notas[1]} nota(s) de R$ 50.00\n{notas[2]} nota(s) de R$ 20.00\n{notas[3]} nota(s) de R$ 10.00\n{notas[4]} nota(s) de R$ 5.00\n{notas[5]} nota(s) de R$ 2.00\nMoedas:\n{notas[6]} moeda(s) de R$ 1.00\n{notas[7]} moeda(s) de R$ 0.50\n{notas[8]} moeda(s) de R$ 0.25\n{notas[9]} moeda(s) de R$ 0.10\n{notas[10]} moeda(s) de R$ 0.05\n{notas[11]} moeda(s) de R$ 0.01')