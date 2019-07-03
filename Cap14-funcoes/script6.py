# escopo de variaveis
# global vs local


num = 1000  # global

def valores(num2):
    """Documentar a função - info pro colegas
        Essa funcao recebe uma variavel e faz a soma
        com outra variavel ...
    """
    global num
    # num = 2000  # local
    print('Num dentro da funçao:{}'.format(num))
    print('Valores somados: {}'.format(num + num2))


valores(3000)

print()
print('Num fora da função:{}'.format(num))
print(valores.__doc__)


for x in dir(str):
    print(x)
