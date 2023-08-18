from time import sleep

def contador(inicio, fim, passo):
    print('==' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    for c in range(inicio, fim, passo):
        sleep(0.5)
        print(f'{c} ', end='')
    print('FIM!')


contador(1, 11, 1)
contador(10, 0, -2)

print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
