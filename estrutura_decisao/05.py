# Faça aquele programinha classico de ver a média de um aluno e ver se ele passou ou não.
print('Vamos coletar as notas do aluno para ver se ele passou ou não.')
nota1 = float(input('Digite aqui a 1° nota do aluno: '))
nota2 = float(input('2° nota do aluno: '))
nota3 = float(input('3° nota do aluno: '))
media = (nota1 + nota2 + nota3) / 3
if media < 5:
    print(f'A média do aluno foi {media:.1f}. O aluno foi reprovado!')
elif media < 7:
    print(f'A média do aluno foi {media:.1f}. O aluno está de recuperação!')
elif media < 10:
    print(f'A média do aluno foi {media:.1f} O aluno foi aprovado!')
else:
    print(f'A média do aluno foi {media:.1f} O aluno foi aprovado com excelência!')
