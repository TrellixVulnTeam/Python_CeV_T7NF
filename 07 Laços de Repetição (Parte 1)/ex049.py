n = int(input('Informe um número para ver sua tabuada: '))
print('-' * 12)
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n * c))
print('-' * 12)
