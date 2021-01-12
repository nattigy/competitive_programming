def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def factorial2(n):
    if n == 0:
        return 1
    res = 1
    for i in range(n, 1, -1):
        res *= i
    return res


print(factorial2(5))
