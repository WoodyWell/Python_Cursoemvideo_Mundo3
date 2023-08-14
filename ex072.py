numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    escolha = int(input('Escolha um número entre 0 e 20: '))
    if escolha > 20 or escolha < 0:
        print('Você digitou um número fora do intervalo. Tente novamente')
    else:
        break
print(f'Você digitou o número: {numeros[escolha]}')
