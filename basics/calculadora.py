numero1 = input("Digite um número:")
numero2 = input("Digite outro número:")

print(f'{"*" * 100}')
print("\tOperacoes disponiveis:\n\t\t+ para adicão\n\t\t- para subtracão\n\t\t* para multiplicao\n\t\t/ para divisão")
print(f'{"*" * 100}')

operacao = input("\nDigite a operacão desejada:")

equacao = f'{numero1} {operacao} {numero2}'

resultado = eval(equacao)

print(f'\n{"*" * 100}\n')
print(f'O resultado é {resultado:.2f}')
print(f'\n{"*" * 100}')
