

# defs
# def soma(x, y): return x + y
# print(soma(20,30))
#
# # lambdas
#
# s = lambda x, y: x+ y
# print(s(20,30))
# print(s(2043,30))
#
# def somas(x, y):
#     s1 = lambda x,y:x+y
#     m = lambda x,y: x * y

# return , yield#
def generator():
    for i in range(10):
        yield (i)

for number in generator():
    print(number)