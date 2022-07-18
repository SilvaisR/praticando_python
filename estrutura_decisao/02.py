# Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input('Digite aqui um valor, pode ser positivo ou negativo: ')) 

if num > 0:
    print('O número é positivo!') 
elif num < 0:
    print('O número é negativo!') 
else:
    print('O número é neutro.') 
    