from datetime import date
while True:
    dados = dict()
    dados['nome'] = str(input('Nome: '))
    dados['idade'] = date.today().year - int(input('Ano de nascimento: '))
    dados['ctps'] = int(input('Nº da Carteira de Trabalho: '))
    if dados['ctps'] == 0:
        break
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - date.today().year)
    break
print(dados)
print('=='*30)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}.')
