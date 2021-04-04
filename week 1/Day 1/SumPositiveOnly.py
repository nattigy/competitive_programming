def SumPositiveOnly(a, b):
    carry = 0
    res = ""
    summ = 0
    num1 = a[::-1]
    num2 = b[::-1]

    app = abs(len(a) - len(b))
    if len(a) > len(b):
        num2 = num2 + ("0" * app)
    else:
        num1 = num1 + ("0" * app)

    for i in range(len(num1)):
        summ = int(num1[i]) + int(num2[i])
        res = res + (str((summ % 10) + carry))
        carry = summ // 10

    return res[::-1]


# print(SumPositiveOnly("123456", "123"))
