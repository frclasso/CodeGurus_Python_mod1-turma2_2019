

str = ''''Lorem Ipsum is simply dummy text of the printing and typesetting 
industry. Lorem Ipsum has been the industry's standard dummy text ever 
since the 1500s, when an unknown printer took a galley of type and scrambled
 it to make a type specimen book. It has survived not only five centuries, 
but also the leap into electronic typesetting, remaining essentially 
unchanged. It was popularised in the 1960s with the release of Letraset
 sheets containing Lorem Ipsum passages, and more recently with desktop 
 publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''

# replace

for letra in str:
    if letra == 'a':
        str = str.replace('a', '@')
    elif letra == 'e':
        str = str.replace('e', '3')
    elif letra == 'i':
        str = str.replace('i', '1')
    elif letra == 'm':
        str = str.replace('m', '#')
    elif letra == 'w':
        str = str.replace('w', '5')
    elif letra == 's':
        str = str.replace('s', 'z')


print(str)

f = open('textocriptografado.txt', 'w')
f.write(str)
f.close()

