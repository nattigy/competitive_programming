from SumPositiveOnly import SumPositiveOnly


def Multiply(a, b):
    carry = 0
    summ = []
    res = ""
    index = 0

    if a == "0" or b == "0":
        return "0"

    for i in a[::-1]:
        for j in b[::-1]:
            res = str(((int(i) * int(j)) + carry) % 10) + res
            carry = (int(i) * int(j)) // 10
        summ.append(
            str(carry) + res + ("0" * index) if carry != 0 else res + ("0" * index)
        )
        carry = 0
        res = ""
        index += 1

    newSum = ""
    for i in summ:
        newSum = SumPositiveOnly(newSum, i)

    return newSum


print(Multiply("1", "298"))
