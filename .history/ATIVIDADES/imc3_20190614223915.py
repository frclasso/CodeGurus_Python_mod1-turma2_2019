#!/usr/bin/env python3
# -*-coding:utf-8 -*-

print('*'*70)
print("Bem vinco ao programa de calculo")
print("Do Indice de Massa Corporal IMC")
print('*'*70)

menu = ''
dados_temp = []
while menu != 0:
    menu = int(input("""
            1 - Para inserir novo cadastro;
            2 - Listar cadastro atual;
            3 - Banco de dados anterior;
            4 - Salvar dados atuais;
            0 - Para sair do programa.
        """))
    if menu == 1:
        print('Inserindo novo cadastro')
        nome = input("Digite seu nome: ")
        altura = float(input("Digite sua altura: "))
        peso = float(input("Digite seu peso: "))

        imc = peso / altura ** 2
        imc = '{:.2f}'.format(imc)

        dados_temp.append(nome)
        dados_temp.append(altura)
        dados_temp.append(peso)
        dados_temp.append(imc)
        print()
        print('Dados inseridos com sucesso!')
        print('Nome: {} Altura: {} Peso: {} IMC: {}'.format(nome, altura,peso,imc))
        print()
    elif menu == 2:
        print('Listando cadastro atual')
        for d in str(dados_temp):
            print(','.join(d))
        break;
    elif menu == 3:
        print('Exibindo banco de dados anterior')
        break;
    elif menu == 4:
        print("Dados salvos com sucesso")
        dados_temp = []
        break;
    elif menu == 0:
        print('Saindo')
    else:
        print('Opção não encontrada')
print()
print('Done...')