lista = list()
cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        cont += 1
        if 5 in lista:
            resp = 'Sim'
        else:
            resp = 'Não'
    else:
        print('Número duplicado. Este valor não será considerado.')
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha in 'N':
        break
print('=='*30)
print(f'Você digitou {cont} elementos')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
print(f'O valor 5 foi digitado na lista? {resp}')
