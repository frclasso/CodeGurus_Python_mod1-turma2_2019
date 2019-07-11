#!/usr/bin/env python3

# strings

s = 'Floripa Code Gurus'
print(s[13]) # indexar
print(s.index('Gurus'))
print(s[:7]) # slice/fatia
print(s + ' 2019') # concatenar
#s[8]= 'Brasil'
s1 = 'Brasil' + s[7:]
print(s1)

# verificar membro
print('Floripa' in s)
print('Brasil' in s)
print('Brasil' not in s)

# len -  tamanho da string
print(len(s))
print(len(s1))

for num, letra in enumerate(s, start=1):
    print(letra, end='=')

print()

indice = 0
while indice < len('Floripa Code Gurus'):
    letra = s[indice]
    print(letra, end='/')
    indice += 1

print()
# find
def busca_letra(str, ch):
    indice = 0
    while indice < len(str):
        if str[indice] == ch:
            return indice
        indice += 1
    return -1
print(busca_letra('Floripa Code Gurus', 'C'))

print(str.find('Floripa', 'F'))

print()

# contador
contador = 0
for letra in s:
    if letra == 'F':
        contador += 1
print(contador)

print(str.count('Floripa Floricultura Flores', 'Flor'))
