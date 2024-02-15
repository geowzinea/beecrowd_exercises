""" 
eia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, 
os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
"""

# Recebe os três valores inteiros
n1, n2, n3 = map(int, input().split())

# Coloca os valores em uma lista
lista = [n1, n2, n3]

# Ordena a lista em ordem crescente
crescente = sorted(lista)

# Imprime os valores ordenados em ordem crescente
for item in crescente:
    print(item)

# Imprime uma linha em branco
print()

# Imprime os valores na sequência em que foram lidos
for item in lista:
    print(item)
