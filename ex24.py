codigo = float(input('Digite o código do alimento: '))
quantidade = float(input('Digite a quantidade: '))

if codigo == 1:
    print(f'Total: R${quantidade * 4.00:.2f}')

elif codigo == 2:
    print(f'Total: R${quantidade * 4.50:.2f}')
    
elif codigo == 3:
    print(f'Total: R${quantidade * 5.00:.2f}')
    
elif codigo == 4:
    print(f'Total: R${quantidade * 2.00:.2f}')
    
elif codigo == 5:
    print(f'Total: R${quantidade * 1.50:.2f}')
    