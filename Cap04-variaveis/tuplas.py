
#tuplas

user1 = ('Fabio', '001', 'Diretor')
user2 = ('Maria', '002', 'Gerente')

print('ID:{}, Nome:{}, Cargo: {}'.format(user1[1],user1[0],user1[2] ))
print('ID:{}, Nome:{}, Cargo: {}'.format(user2[1],user2[0],user2[2] ))




users = [user1 ,  user2]

# indices
print(users[0])
print(users[0][0])
chefe = users[0]
print(chefe)

