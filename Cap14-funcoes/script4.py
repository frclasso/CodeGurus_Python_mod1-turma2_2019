
total = 0  # global
# escopo de variaveis

def soma(x, y):
    #global total
    total = x + y  #local
    print('Valor de total dentro da função:{}'.format(total))

soma(10, 20)
print("Valor de total fora função:{}".format(total))
print(f"Valor de total fora função:{total}")

