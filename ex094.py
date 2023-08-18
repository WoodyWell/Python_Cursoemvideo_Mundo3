pessoa = dict()
todos = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Digite a idade: '))
    soma += pessoa['idade']
    todos.append(pessoa.copy())
    while True:
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if escolha in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if escolha == 'N':
        break
media = soma / len(todos)
print(f'A) Ao todo temos {len(todos)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f}')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in todos:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista de pessoas que estão acima da média: ', end='')
for p in todos:
    if p['idade'] > media:
        print(f'{p["nome"]} ', end='')
print()