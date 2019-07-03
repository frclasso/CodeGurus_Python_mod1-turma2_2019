
#
# f = open("newfile.txt", 'w')
# str = 'Primeira linha'
# f.write(str)
#
# f.close()

## inserir mais linhas

f = open("newfile.txt", 'r+')
str = ['\nSegunda linhas', '\nTerceira linha']

for line in str:
    f.writelines(line)

f.close()