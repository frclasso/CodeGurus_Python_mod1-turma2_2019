import os

#print(os.getcwd())

os.chdir('/home/fabio-gurus/Desktop/repositories/Floripa_code_gurus_repos/'
         'CodeGurus_Python_mod1-turma2_2019/cap16-arquivos/folder1/imgs')

#print(os.getcwd())

# for files in os.listdir():
#     print(files)


from PIL import Image
image1 = Image.open("aguia - natureza selvagem - #2.jpg")
#image1.show()

# alterar formato
#image1.save('aguia.png')

# salvar varios arquivos
#os.mkdir('back_up_imgs/')

# for f in os.listdir():
#     if f.endswith('.jpg'):
#         # print(f)
#         i = Image.open(f)
#         file_name, f_extensao = os.path.splitext(f)
#         #print(file_name)
#
#
#         # criar uma pasta de backup
#         i.save('back_up_imgs/{}.png'.format(file_name))

os.mkdir('back_up_imgs_700/')
size_300 = (300,300)
size_700 = (700,700)

for f in os.listdir():
    if f.endswith('.jpg'):
        i = Image.open(f)
        file_name, f_extensao = os.path.splitext(f)

        i.thumbnail(size_700)
        i.save('back_up_imgs_700/{}_700x700{}'.format(file_name, f_extensao))