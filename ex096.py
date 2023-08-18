def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é igual a {a}m²')


print('Controle de Terrenos')
print('=='*10)
l = float(input('Digite a LARGURA (m): '))
c = float(input('Digite o COMPRIMENTO (m): '))
area(l, c)