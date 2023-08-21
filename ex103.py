def jogador(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = '0'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('=='*20)
j = str(input('Nome do jogador: '))
g = str(input('Números de gols: '))
jogador(j, g)
