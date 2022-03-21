resultados = []
with open("../dados/cadastro.csv", "r") as arquivo_entrada:
    linhas = arquivo_entrada.readlines()
    linhas = linhas[1:]

    for linha in linhas:
        dados = linha.split(",")
        email = dados[3].replace("\n","")
        resultados.append(f'{dados[1]} {dados[2]}, {email}\n')

with open("../dados/cadastro_saida.csv", "w") as arquivo_saida:
    for resultado in resultados:
        arquivo_saida.write(resultado)
