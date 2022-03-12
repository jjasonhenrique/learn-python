familia = {
    'pai': 'Joao',
    'mae': 'Maria',
    'filho1': 'Jason',
    'filho2': 'Igor',
    'filho3': 'Rafael'
}


#print(familia)

valores = familia.items()

for valor in valores:
    print(f'O grau de parentesco é {valor[0]} e o nome dele é {valor[1]}.')