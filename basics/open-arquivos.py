text = "Jornada Python 2\nTeste Quebra"

arquivo = open("//Users//jason.rodrigues//Documents//DevOps//Github//learn-python//dados//teste.txt", "a")

retorno = arquivo.write(text)

print("Executado com sucesso")

arquivo.close()

print("Arquivo fechado com sucesso")