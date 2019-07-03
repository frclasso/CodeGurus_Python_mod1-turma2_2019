#!/usr/bin/env python3

# revisão
# def =  definition
# nome
# () vem argumentos, pode ter 0 ou mais de 1
# : bloco da função

# definindo a função
def soma():
    pass


# chamada da função - executar
#soma()

# saida,
# print
# return

def dados():
    nome = input('Digite seu nome: ')
    print(nome)
#dados()

def dados2():
    nome = input('Digite seu nome: ')
    return nome

#n = dados2()

# argumentos, pode ter 0 ou mais de 1

def dados3(nome, sobrenome, telefone):  #   argumentos requeridos
    print('Seus dados')
    # nome = input('Digite seu nome: ')
    # sobrenome = input('Digite seu sobrenome: ')
    # telefone = input('Digite seu telefone: ')
    return nome, sobrenome, telefone

#print(dados3('Fabio', 'Classo', '4899999999'))

def dados4(nome, sobrenome, cadastro='ativo'): # Argumento padrao /default
    return nome,sobrenome,cadastro

# print(dados4('Fabio', 'Classo', 'inativo'))



# Argumentos de palavra chave
def dados5(nome, sobrenome, telefone):
    print(f'Seu nome é: {nome}')
    print(f'Seu sobrenome é: {sobrenome}')
    print(f'Seu telefone é: {telefone}')

# print(dados5(nome='Fabio', sobrenome='Classo', telefone='489999777'))

#dados5(sobrenome='Classo',telefone='489999777', nome='Fabio')

# argumentos de tamanho de variavel
def dados6(*args):   # * tupla de dados
    return args

#print(dados6('Fabio', 'Classo', '4899999999', ' email.com'))


def dados7(**kwargs): # **kwargs - dicionario
    return kwargs

#print(dados7(nome='Fabio', sobrenome='Classo', email='email.com'))


def dados_totais(nome, sobrenome, situacao='ATIVO', *args, **kwargs):
    return nome, sobrenome, situacao, args, kwargs

print(dados_totais('Fabio','Classo','INATIVO',70, 80,90,100, email='fabio@com'))

