#!/usr/bin/env python3
# -*-coding:utf-8 -*-

print('*'*70)
print("Bem vinco ao programa de calculo")
print("Do Indice de Massa Corporal IMC")
print('*'*70)

menu = input("""
            1 - Para inserir novo cadastro;
            2 - Listar cadastros;
            0 - Para sair do programa.
        """)

dados_temp = []
while menu != '0':
    if menu == '1':
        nome = input("Digite seu nome: ")
        altura = float(input("Digite sua altura: "))
        peso = float(input("Digite seu peso: "))

        imc = peso / altura ** 2
        imc = '{:.2f}'.format(imc)

        dados_temp.append(nome)
        dados_temp.append(altura)
        dados_temp.append(peso)
        dados_temp.append(imc)

        with open('imc.csv', 'a') as file:
            for data in str(dados_temp):
                file.writelines(data)
            file.writelines('\n')
        print()
        print('Dados inseridos com sucesso!')
        print('Nome: {} Altura: {} Peso: {} IMC: {}'.format(nome, altura,peso,imc))
        print()
        menu = input("""
                    1 - Para inserir novo cadastro;
                    2 - Listar cadastros;
                    0 - Para sair do programa.
                """)
    elif menu == '2':
        with open('imc.csv', 'r') as file:
            reader = file.readlines()
            for data in reader:
                print(data, end='')
        print()
        menu = input("""
                    1 - Para inserir novo cadastro;
                    2 - Listar cadastros;
                    0 - Para sair do programa.
                """)
    elif menu == '0':
        print('Saindo programa, bye bye')
        print('*' * 70)
    else:
        print('Opcao nao encontrada')
        menu = input("""
                    1 - Para inserir novo cadastro;
                    2 - Listar cadastros;
                    0 - Para sair do programa.
                """)


