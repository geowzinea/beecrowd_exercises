""" 
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

MAIORAB = (a+b+abs(a-b)) / 2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
"""

# Entrada dos três valores inteiros
a, b, c = map(int, input().split())

# Cálculo do maior valor entre a e b usando a fórmula fornecida
maior_ab = (a + b + abs(a - b)) // 2

# Cálculo do maior valor entre o resultado anterior e c
maior = (maior_ab + c + abs(maior_ab - c)) // 2

# Impressão do resultado
print(f"{maior} eh o maior")