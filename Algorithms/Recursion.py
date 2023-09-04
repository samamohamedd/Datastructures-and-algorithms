# using loops:
def factorial(num):
    i = num
    fact = 1
    while i > 1:
        fact = fact * i
        i -= 1
    return fact


# using recrsion:
def factorial2(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


# more efficient solution using tail-recursion:
def factorial3(n, acc=1):
    if n == 0:
        return acc
    return factorial3(n - 1, (n * acc))


l = [0, 1]


def fibonacci(n):
    if len(l) >= n:
        return l[n - 1]
    l.append(l[len(l) - 1] + l[len(l) - 2])
    return fibonacci(n)


print(fibonacci(6))

print(factorial(6))
print(factorial2(6))
print(factorial3(6))
