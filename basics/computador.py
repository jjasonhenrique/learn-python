computador = {
    'cpu': 'Intel i7',
    'ram': 'DDR 4GB',
    'disk': 'SSD 480GB'
}

print(f'Montagem do Computador v1: {computador}')

computador['Placa de Video'] = 'Nvidia GForce'

print(f'Montagem do Computador v2: {computador}')

computador.update({'Placa de Som': 'Placa de Som OffBoard', 'Fonte': 'Fonte 850W Real'} )

print(f'Montagem do Computador v3: {computador}')

computador.clear()

print(f'Montagem do Computador v4: {computador}')