def soma(*numeros):
    resultado = 0

    for numero in numeros:
         resultado += numero

    return resultado


resultado = soma(5, 5, 10, 30)
print(resultado)


