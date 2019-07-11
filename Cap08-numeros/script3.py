#!/usr/bin/env python


import random

# random  gera valores entre 0 e 1
print(random.random())

# choice
pets = ['cat','dog', 'bear', 'fish', 'rat']
print(random.choice(pets))

# shuffle
cards = ['Jack','Queen','Ace', 'King']
random.shuffle(cards)
print(cards)

#randrange

numeros = random.randrange(5) # sorteia dentro do intervalo determinado
print(numeros)

megasena = random.sample(range(1, 62), 6)

print(f'Numeros sorteados: {sorted(megasena)}')
