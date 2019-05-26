

# Leitor de dados de teste.csv
# o arquivo a ser lido tem que estar no mesmo diretorio

leitor = open('teste.csv', 'r') # r/read/leitura
l = leitor.read()  # le todo conteudo
print(l)

leitor.close()

print('Dados lidos com sucesso.')