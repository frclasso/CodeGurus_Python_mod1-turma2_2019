

arquivo = open("loren.txt", "r")
# print(arquivo.name)
# print(arquivo.mode)

str = arquivo.read(40)
print(str)
posicao = arquivo.tell() # checa a posicao do cursor
print(f"Posição atual do cursor:{posicao}")

print()
#print(arquivo.read())
arquivo.seek(0)  # pro inicio
posicao = arquivo.tell() # checa a posicao do cursor
print(f"Posição atual do cursor:{posicao}")

print(arquivo.read())
posicao = arquivo.tell() # checa a posicao do cursor
print(f"Posição atual do cursor:{posicao}")

arquivo.close()