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
        break;
    elif menu == 2:
        print('Listando cadastro atual')
        break;
    elif menu == 3:
        print('Exibindo banco de dados anterior')
        break;
    elif menu == 4:
        print("Dados salvos com sucesso")
        dados_temp = []
        break;
    else:
        print('Opção não encontrada') 
print('Done...')