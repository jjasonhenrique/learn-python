import random

clientes = ["Jimmy", "Kim", "John", "Stacie", "Jason"]
sabores = ["Baunilha", "Chocolate", "Morango", "Prestígio", "Torta de Limão"]

vencedor = random.choice(clientes)
sabor = random.choice(sabores)

print(f"O vencedor é {vencedor} e o sabor é {sabor}")

quer_cereja = input("Quer uma cereja? (S/N) ")

if quer_cereja == "S":
    print(f"Saindo um sundae de {sabor} com cereja")
elif quer_cereja == "N":
    print(f"Saindo um sundae de {sabor}")
else:
    print("Opcao invalida")



