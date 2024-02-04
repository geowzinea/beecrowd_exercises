A = int(input())
B = int(input())
C = int(input())
D = int(input())

soma1 = A + B
soma = C + D

if B > C and D > A and soma > soma1 and A % 2 == 0:
    print('Valores aceitos')
else: 
    print('Valores não aceitos')