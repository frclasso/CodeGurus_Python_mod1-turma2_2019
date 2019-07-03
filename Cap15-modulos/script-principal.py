#
import fibonacci

f = fibonacci
#print(fibonacci.x)
# print(dir(f))

print(f.fib(fibonacci.x))



from fibonacci import fib

print(fib(100))

from fibonacci import fib, x

print(x)
print(fib(x))