
# 1 junho
# menu restaurante
# opcoes de pratos - # listas

frutos_do_mar = [
    ['Lagosta, ao molho de camarao'],
    ['Camarao alho e oleo'],
    ['Tainha recheada']
]
# massas
# saladas
# carnes

#print(frutos_do_mar[0])  # teste


menu = int(input('Escolha uma opcao: '))
if menu == 0:
    print('Sair')
elif menu == 1:
    print('Voce escolheu Frutos do Mar')
    print(frutos_do_mar[0])
    print(frutos_do_mar[1])
    print(frutos_do_mar[2])
elif menu == 2:
    print('Voce escolheu Massas')
elif menu == 3:
    print('Voce escolheu Saladas')
elif menu == 4:
    print('Voce escolheu Carnes')
else:
    print('Voce precisa escolher uma opcao entre 1 e 4 ou zero para sair')