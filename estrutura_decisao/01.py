# Faça um programa que peça dois números e imprima o maior deles.
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
maior = num1
if num2 > maior:
    print (f'O maior dos dois é: {num2}') 
else:
    print(f'O maior dos dois é: {maior}') 
