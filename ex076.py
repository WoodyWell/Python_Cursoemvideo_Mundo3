print('='*30)
print('LISTA DE PREÇOS'.center(30))
print('='*30)
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estejo', 25.00, 'Transferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}R$', end='')
    else:
        print(f'{lista[pos]:>7.2f}')
