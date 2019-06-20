#!/usr/bin/emv python3


# Passagem por valor
def changeme(mylist):
    """Essa função Não altera a lista passada como argumento"""
    mylist = [10,20,30,40]
    print("Valores detro da função: {}".format(mylist))


#
mylist = [100,200,300,400]

changeme(mylist)
print()
print("Valores fora da função: {}".format(mylist))
print()

# Passagem por referencia
def changeme2(mylist2):
    """Essa função  altera a lista passada como argumento"""
    mylist2[2] = 500
    print("Valores detro da função: {}".format(mylist2))


mylist2 = [100,200,300,400]

changeme2(mylist2)
print()
print("Valores fora da função: {}".format(mylist2))
