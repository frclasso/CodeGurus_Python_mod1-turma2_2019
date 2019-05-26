

# variaveis  - nome, sobrenome email

nome = input("Digite seu nome:")
sobrenome = input("Digite seu sobrenome:")
email = nome + sobrenome + '@companyname.com'
# inputs - entrada de dados


# imprimir dados

print(email)

# salvar dados
#open ==> r, w , a, b
arquivo = open('teste.csv', 'a') # append
arquivo.write(nome + ',' + sobrenome + ',' + email + ','+ '\n')
arquivo.close() 

print("Cadastro concluido com sucesso")