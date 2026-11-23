it = iter([1, 2, 3])
print(next(it))
print(next(it))
print(next(it))
print(next(it))

it = iter([1, 2, 3])
while True:
        try:
            print(next(it))
        except StopIteration:
            print("Iteration is finish")
        break


def fib_list(n):
    result = []
    a, b = 0, 1 

    for _ in range(n):
         result.append(a)
         a, b = b, a + b
    return result

def fib_gen(n):
     a, b = 0, 1 
     for _ in range(n):
          print("about to yield", a)
          yield a 
          a, b = b, a + b

print("Fibonacci list")
print(fib_list(10))

print("Fibonacci genretor")
print(fib_gen(10))

print("return type")
print(type(fib_list(10)))
print(type(fib_gen(10)))

print("frist loop")
g = fib_gen(5)
for num in g:
     print(num)

print("second loop")
for num in g:
     print(num)

