n = 5
fact = 1

while n > 1:
    fact = fact * n
    n -= 1

print(fact)


def rfact(n):
    if n < 1:
        return 1
    else:
        number = n * rfact(n-1)
        return number

print(rfact(5))


# NOTE: fib() is way faster than rfib(), recursion is very useful but need to be smart with it.
def fib(n): 
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

print(fib(5)) 


def rfib(n):
    if n <= 1:
        return n
    else:
        return (rfib(n-1) + rfib(n-2))
    
print(rfib(5))