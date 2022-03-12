from random import randint
capacida_maxima_balde = 1000

balde = 0

while balde <= capacida_maxima_balde:
    copo = randint(85, 95)
    print(f'O volume do copo é de {copo}mls')

    balde += copo
    print(f'O volume do balde é {balde}mls\n')

print(f'O volume do balde ultrapassou {balde -1000}mls pois o ultimo copo tem {copo}mls')


