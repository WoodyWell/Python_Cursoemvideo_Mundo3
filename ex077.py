palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in palavras:
    print(f'\nNa palavra {c} temos: ', end='')
    for letras in c:
        if letras in 'AEIOU':
            print(f'{letras}', end='')
