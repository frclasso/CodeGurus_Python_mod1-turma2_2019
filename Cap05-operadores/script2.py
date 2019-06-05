#associacao

# In, Not in


l = ['Fabio', 'Matheus', 'Python', 'Rodolfo', 2019]

print('Fabio' in l)
print('Mario' in l)
print(2019 in l)
print(2018 not in l)

# Identidade  Is , Is not
print('-'* 70)
a = 20
b = 20
print(a is b)
print(id(a))
print(id(b))

l2 = l #shallow copy
print('-'* 70)
print(l2 is l)
print(id(l))
print(id(l2))

print('-'* 70)
l2 = l[:] #deep copy
print(l2 is l)
print(id(l))
print(id(l2))

print('-'* 70)
l2 = l[:] #deep copy
print(l2 is not l)
print(id(l))
print(id(l2))