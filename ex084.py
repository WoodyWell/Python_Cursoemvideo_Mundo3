todos = list()
pessoa = list()
cont = maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(todos) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    todos.append(pessoa[:])
    pessoa.clear()
    cont += 1
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha in 'N':
        break
print('=='*30)
print(f'Ao todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {maior:.1f}kg. Peso de >>> ', end='')
for p in todos:
    if p[1] == maior:
        print(f'{p[0]}...', end='')
print(f'\nO menor peso foi de {menor:.1f}kg. Peso de >>> ', end='')
for p in todos:
    if p[1] == menor:
        print(f'{p[0]}...', end='')
