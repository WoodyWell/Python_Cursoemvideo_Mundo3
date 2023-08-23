def numint(msg):
    while True:
        try:
            n = int(input(msg))
            break
        except (TypeError, ValueError):
            print(f'\033[31mErro! Favor digitar um número inteiro!\033[m')
            continue
    return n

def numfloat(msg):
    while True:
        try:
            n = float(input(msg))
            break
        except (TypeError, ValueError):
            print(f'\033[31mErro! Favor digitar um número real!\033[m')
            continue
    return n


n1 = numint('Digite um número inteiro: ')
n2 = numfloat('Digite um número Real: ')
print(f'Você digitou o número inteiro {n1} e o número real {n2}')
