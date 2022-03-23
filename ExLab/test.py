a, b, c, d = input().split()
A = int(a)
B = int(b)
C = int(c)
D = int(d)

hora = C - A
min = D - B

if A == C and B == D:
    hora = 24
    min = 0
elif A< C and B > D:
    hora = 0
elif hora < 0:
    hora = 24 + hora
elif min < 0:
    min = 60 + min
print(f"O JOGO DUROU {hora} HORA(S) E {min} MINUTO(S)")