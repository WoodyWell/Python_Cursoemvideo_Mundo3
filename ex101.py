def votacao(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        print(f'Com {idade} anos: Você não VOTA!')
    elif idade >= 16 and idade < 18 or idade >= 65:
        print(f'Com {idade} anos: O voto é OPCIONAL')
    else:
        print(f'Com {idade} anos: O voto é OBRIGATÓRIO')


print('=='*15)
votacao(int(input('Em que ano você nasceu? ')))
