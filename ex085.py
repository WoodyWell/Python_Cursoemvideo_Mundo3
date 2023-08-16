todos = [[], []]
num = 0
for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        todos[0].append(num)
    else:
        todos[1].append(num)
print('=='*30)
print(f'Os valores pares digitados foram: {sorted(todos[0])}')
print(f'Os valores ímpares digitados foram: {sorted(todos[1])}')
