from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano

print('O atleta tem {} anos'.format(idade))

if idade <=9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JÚNIOR')
elif idade <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')