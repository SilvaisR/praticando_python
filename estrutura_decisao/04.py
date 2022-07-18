# Faça um programa que leia uma letra e verifique se a letra é uma vogal ou uma consoante.
vogais = ['a', 'e', 'i', 'o', 'u']
letra = str(input('Digite aqui a letra: ')).strip().lower()
if letra in vogais:
    print('A letra é vogal.')
else:
    print('A letra é consoante.')
