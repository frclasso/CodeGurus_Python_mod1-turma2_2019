

# argumetos requeridos
def insere_dados(nome):
    return nome


# print(insere_dados('Fabio'))

# palavra chave - key words arguments
def printInfo(nome, idade):
    print(f"Nome:{nome}")
    print(f"Idade:{idade}")

# printInfo(idade=44, nome='Fabio')
# printInfo(nome='Fabio', idade=45)  # palavra chave

# argumento padrão - default
def Info(nome, idade=44):
    print(f"Nome:{nome}")
    print(f"Idade:{idade}")

# Info('Fabio')

# args - retorna um tupla de valores - argumento de tamanho variavel
def dados(*args):
    print(args)


dados("Fabio", 44, 'Brasil', 'fabio@email.com')


# **kwargs - retorna um dicionario
def Data(**kwargs):
    print(kwargs)

Data(nome='Fabio', idade=44, email='fabio@email.com')


def final(nome, *args, **kwargs):
    idade = 45
    return nome,idade ,args, kwargs

print(final('Fabio',20,30,40, email='fabioclasso@email.com', telefone='99999999'))