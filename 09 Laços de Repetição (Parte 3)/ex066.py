cont = soma = 0
while True:
    n = int(input('Informe um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} números informados é {soma}')