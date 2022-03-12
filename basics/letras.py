

teste = {
    'Nome': 'Jason',
    'Idade': 36,
    'Compras': [{
        'id': '123',
        'produto': 'Notebook'
    }]
}
id = teste['Compras'][0]['id']
produto = teste['Compras'][0]['produto']

print(produto, id)

teste['Nome'] = 'Rafael'
print(teste['Nome'])