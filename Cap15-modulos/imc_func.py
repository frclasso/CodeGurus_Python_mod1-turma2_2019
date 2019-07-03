#!/usr/bin/env python3

## Calculo de IMC

print(" Programa de calculo de IMC")
print('-'*79)

dados_temp =[]
menu =''

def insere_dados():
    print('Inserindo novo cadastro')
    nome = input('Digite seu nome: ')
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))

    imc = peso / altura ** 2
    imc = '{:.2f}'.format(imc)
    dados_temp.append(nome)
    dados_temp.append(altura)
    dados_temp.append(peso)
    dados_temp.append(imc)
    print('Dados salvos com sucesso')
    print('Nome: {} Altura: {} Peso: {} e IMC: {}'.format(nome, altura, peso, imc))
    print()

def listar_cadastro_atual():
    print('Listar cadastro atual')
    for d in str(dados_temp):
        print(','.join(d), end='')
    print()


def visualizar_dados_anteriores():
    print('Visualizando banco de dados anterior')
    with open('imc.csv', 'r') as file:
        reader = file.readlines()
        for data in reader:
            print(data, end='')


def salvar_Dados():
    with open('imc.csv', 'a') as file:
        for data in str(dados_temp):
            file.writelines(data)
        file.writelines('\n')
    print('Dados salvos com sucesso!')


def sair():
    print('Programa finalizado.')



