from time import sleep
def maior(* num):
    print('=='*25)
    print('Analisando os valores...')
    sleep(0.5)
    for valor in num:
        print(f'{valor} ', end='')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior número é: {max(num)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)