def factorial(n):
    if n < 0:
        return None
    return 1 if n == 0 else n * factorial(n - 1)


def factorial2(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    res = 1
    for i in range(n, 1, -1):
        res *= i
    return res


print(factorial(-5))
