jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = list()
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('=='*30)
print(jogador)
print('=='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'>>> Na partida {i+1} fez {v} gols.')
print(f'No total foram {jogador["total"]} gols marcados.')
