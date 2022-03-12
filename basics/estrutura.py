idade = input("Digite a sua idade:")

print(f'{"*" * 100}')
print(
    f'\tM - para Masculino\n'
    f'\tF - para Feminino'
)
print(f'{"*" * 100}\n')
sexo = input("Digite seu sexo:")
print(f'\n{"*" * 100}\n')

if sexo.upper() == "M":
    if int(idade) >= 65:
        print("Aposentadoria Concedida")
    else:
        print(f"Aposentadoria Negada. Aguarde mais {65 - int(idade)} anos")

elif sexo.upper() == "F":
    if int(idade) >= 60:
        print("Aposentadoria Concedida")
    else:
        print(f"Aposentadoria Negada. Aguarde mais {60 - int(idade)} anos")

else:
    print("Opcão Invalida ! Favor tentar novamente")

