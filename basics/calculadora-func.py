def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

num1: int = int(input("Insira um número:"))
num2: int = int(input("Insira outro número:"))

print(f'\tDigite o nome da Operacão:\n')
print(f'\t\t1 - Soma\n')
print(f'\t\t2 - Subtracao\n')
print(f'\t\t3 - Multiplicaao\n')
print(f'\t\t4 - Divisao\n')

cod_opera = input("Digite o numero da Operacão:\t")

opcao_invalida: list = [1, 2, 3, 4]

match cod_opera:
    case "1":
        resultado = soma(num1, num2)
        print(f'O resultado da soma é {resultado}')
    case "2":
        resultado = subtracao(num1, num2)
        print(f'O resultado da subtracao é{resultado}')
    case "3":
        resultado = multiplicacao(num1, num2)
        print(f'O resultado da multiplicacao {resultado}')
    case "4":
        resultado = divisao(num1, num2)
        print(f'O resultado da divisao{resultado}')
    case _:
        print("Opcao Invalida. Tente novamente")









