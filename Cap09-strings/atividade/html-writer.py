import urllib.request

page = urllib.request.urlopen('https://docs.python.org/')

with open('pythondocs.html', 'w') as file:
    for line in page:
        file.write(str(line, encoding='utf-8'))

print('Feito...')

## olhar bibliotecas
# urllib
# BeatifulSoup