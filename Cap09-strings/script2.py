
# classificar caracteres
s = 'Floripa Code Gurus'
print(s.lower())
print(s.upper())
print(s.title())
print(s.capitalize())
print(s.isdigit())

# format string

escola = 'Floripa Code Gurus'
curso = 'Python'
ano = 2019

# python2
print('%s - %s, ano: %d'% (escola, curso, ano))

#python3
print('{} - {}, ano: {}'.format(escola, curso, ano))
#python3.6.5
print(f'{escola} - {curso}, ano: {ano}')


my_string ='****Floripa Code Gurus****'
print(my_string.strip('*'))
print(my_string.lstrip('*')) # elimina do lado esquerdo/left
print(my_string.rstrip('*')) # do lado direito /right

print()
# replace
escola = 'Floripa Code Gurus'
print(escola.replace('Floripa', 'Brasil'))

