num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = int(input('Digite mais um número inteiro: '))
num4 = int(input('Digite o último número inteiro: '))
numeros = (num1, num2, num3, num4)
cont = 0
print('=-='*20)
print(f'Você digitou os valores: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado.')
if numeros[0] % 2 == 0:
    cont += 1
if numeros[1] % 2 == 0:
    cont += 1
if numeros[2] % 2 == 0:
    cont += 1
if numeros[3] % 2 == 0:
    cont += 1
print(f'Os valores pares digitados foram: {cont}')
