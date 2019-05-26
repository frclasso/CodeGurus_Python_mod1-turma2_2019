

# set = {,}

num = {1,2,3,4}
um = set(num)
vazio = set()

print(type(num))
print(type(um))
print(type(vazio))

a = {9,1,2,3,4,1,2,3,5,2,3,2,4,6,3,4,5,6,7,3,4,4,5,6,8,2,3,3,4,6,7}
print(a)

frutas = {'maça', 'pera', 'uva', 'banana',
          'melão', 'maça', 'pera', 'uva',
          'banana','melão',
          'melão', 'maça', 'pera', 'uva'}

print(frutas)

# operações de conjunto
c = {3,4,5,10}
d = {4,5,6,7,8,9}

print(c.union(d)) # unição
print(c.difference(d)) # direfença
print(c.intersection(d)) # interseção
print(c.__ixor__(d)) # retorna os diferentes

print(c | d) # uniao
print(c -  d) # diferenca
print(c & d) # intersecao
print(c ^ d) # XOR


lista = [1,2,3,4,5]
t = tuple(lista)
print(type(t))
l = list(t)
print(type(l))

z = 1000
print(type(z))
print(z)
print(float(z))
print(str(z))

a = str(z)
x = 10
y = float(x)
print(type(y))
print(int(y))



