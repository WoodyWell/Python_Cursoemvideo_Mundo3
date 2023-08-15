num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    elif n in num:
        print('Número já cadastrado.')
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha in 'Nn':
        break
print(f'Você digitou os números: {sorted(num)}')
