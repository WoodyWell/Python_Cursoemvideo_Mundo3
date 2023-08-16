alunos = list()
todos = list()
escolha= ''
while True:
    alunos.append(str(input('Nome: ')))
    alunos.append(float(input('Nota 1: ')))
    alunos.append(float(input('Nota 2: ')))
    alunos.append(float((alunos[1] + alunos[2]) / 2))
    todos.append(alunos[:])
    alunos.clear()
    escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if escolha in 'N':
        break
print('=='*20)
print(f'{"Nº":<5}{"NOME":<10}{"MÉDIA":<5}')
for c, v in enumerate(todos):
    print(f'{c:<5} {v[0]:<10} {v[3]:<5}')
print('=='*20)
while True:
    nota = int(input('Mostrar as notas de qual aluno? (Digite 999 para finalizar): '))
    if nota == 999:
        print('FINALIZANDO...')
        break
    if nota <= len(todos) -1:
        print(f'As notas de {todos[nota][0]} são [{todos[nota][1]}, {todos[nota][2]}]')
        print('--' * 20)
print('VOLTE SEMPRE!')