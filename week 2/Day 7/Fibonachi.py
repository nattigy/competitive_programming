def Fibonachi(n):
    return n if n <= 1 else Fibonachi(n - 2) + Fibonachi(n - 1)


def Fibonachi2(n):
    if n <= 1:
        return n
    n1 = 0
    n2 = 1
    for i in range(n - 1):
        summ = n1 + n2
        n1 = n2
        n2 = summ
    return n2


print(Fibonachi(6))