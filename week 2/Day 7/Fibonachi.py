def Fibonachi(n):
    if n <= 1:
        return n
    return Fibonachi(n - 2) + Fibonachi(n - 1)


print(Fibonachi(100))