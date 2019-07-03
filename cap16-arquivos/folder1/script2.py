

import os

# print(os.getcwd())

os.chdir('/home/fabio-gurus/Desktop/repositories/Floripa_code_gurus_repos/'
         'CodeGurus_Python_mod1-turma2_2019/cap16-arquivos/folder1/imgs/'
         'back_up_imgs')


for f in os.listdir():
    #print(f)
    nome, extensao = os.path.splitext(f)
    # print(nome)
    # print(nome.split('-'))
    animal, titulo, numeros = nome.split('-')
    #print(animal)
    #print('{}-{}-{}'.format(animal, titulo, numeros))

    #print(titulo)
    animal = animal.strip()
    titulo = titulo.strip()
    numeros = numeros.strip()

    #print(numeros)
    numeros = numeros.strip()[1:]
    #print(numeros)

    novo_nome = '{}_{}_{}{}'.format(numeros,titulo, animal, extensao)
    print(novo_nome)