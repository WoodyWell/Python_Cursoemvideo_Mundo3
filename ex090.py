dados = dict()
dados['aluno'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados["aluno"]}: '))
if dados['média'] >= 7:
    dados['situação'] = 'Aprovado'
elif 5 <= dados['média'] < 7:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'
print('=='*30)
print(f'Nome do aluno: {dados["aluno"]}')
print(f'Média de {dados["aluno"]}: {dados["média"]}')
print(f'Situação do aluno: {dados["situação"]}')
