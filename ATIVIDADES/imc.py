
# calcular IMC

nome = input("Digite seu nome: ")
altura = int(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

# -----------
# imc - calculo


# lista com dados

# lista com dados   -  append


# imprimir o resultado

# salvar
arquivo = open('imc.csv', 'a') # append
arquivo.write(nome + ',' + altura + ',' + peso + ','+ imc + ','+ '\n')
arquivo.close()