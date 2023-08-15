lista = list()
pares = list()
ímpares = list()
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        ímpares.append(num)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print('=='*30)
print(f'A lista completa dos valores é: {lista}')
print(f'A lista de valores pares é: {pares}')
print(f'A lista de valores ímpares é: {ímpares}')
