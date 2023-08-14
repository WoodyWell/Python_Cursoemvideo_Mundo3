times = ('Newcastle', 'Brighton', 'Manchester City', 'Arsenal', 'Crystal Palace', 'Fulham', 'Brentford', 'Tottenham',
         'Bournemouth', 'Chelsea', 'Liverpool', 'West Ham', 'Manchester United', 'Wolverhampton',
         'Nottingham Forest', 'Everton', 'Sheffield', 'Luton Town', 'Burnley', 'Aston Villa')
print('=-='*20)
print(f'Lista de times da Premier League: {times}')
print('=-='*20)
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('=-='*20)
print(f'Os quatro últimos colocados são: {times[-4:]}')
print('=-='*20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-='*20)
print(f'O Liverpool está na posição: {times.index("Liverpool")+1}')
