from imc_func import insere_dados, listar_cadastro_atual, visualizar_dados_anteriores,salvar_Dados, sair
import imc_func.menu

menu = imc_func

def menu():
    while menu != 0:
        menu = int(input("""
                1 - Para inserir novo cadastro;
                2 - Listar cadastro atual;
                3 - Banco de dados anterior;
                4 - Salvar dados atuais;
                0 - Para sair do programa
                    """))
        if menu == 1:
            insere_dados()
        elif menu == 2:
            listar_cadastro_atual()
        elif menu == 3:
            visualizar_dados_anteriores()
        elif menu == 4:
            salvar_Dados()
        elif menu == 0:
            sair()
        else:
            print('Opcao encontrada')
    return menu