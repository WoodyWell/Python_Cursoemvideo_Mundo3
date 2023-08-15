expre = str(input('Digite uma expressão: '))
dados = list()
for simb in expre:
    if simb == '(':
        dados.append('(')
    elif simb == ')':
        if len(dados) > 0:
            dados.pop()
        else:
            dados.append(')')
            break
if len(dados) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está incorreta!')
