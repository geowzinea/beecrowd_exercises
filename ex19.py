""" 
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
"""

tempo = int(input())
horas = tempo // 3600
tempo %= 3600
minutos =  tempo // 60
tempo %= 60
segundos = tempo 
print(f'{horas:.0f}:{minutos:.0f}:{segundos:.0f}')