from SumPositiveOnly import SumPositiveOnly


def SumNegativeOnly(a, b):
    num1 = a.split("-")
    num2 = b.split("-")

    print(num1, a.split("-"))
    if num1[0] == "-" and num2[0] == "-":
        return "-" + SumPositiveOnly(num1[1], num2[1])
    if num1[0] != "-" and num2[0] != "-":
        return SumPositiveOnly(num1[0], num2[0])
    if num1[0] == "-" and num2[0] != "-":
        if num1[1] == num2[0]:
            return "0"
        if len(num1[1]) > len(num2[0]):
            return "-" + Subtraction(num1[1], num2[0])
        elif len(num1[1]) == len(num2[0]) and num1[1] > num2[0]:
            return "-" + Subtraction(num1[1], num2[0])
        else:
            return Subtraction(num1[1], num2[0])
    if num1[0] != "-" and num2[0] == "-":
        if num1[0] == num2[1]:
            return "0"
        if len(num1[0]) > len(num2[1]):
            return Subtraction(num1[0], num2[1])
        elif len(num1[0]) == len(num2[1]) and num1[0] > num2[1]:
            return Subtraction(num1[1], num2[0])
        else:
            return "-" + Subtraction(num1[1], num2[0])


def Subtraction(a, b):
    num1 = a
    num2 = b
    if len(a) < len(b):
        num1, num2 = b, a
    elif len(a) == len(b):
        if a < b:
            num1, num2 = b, a

    num1 = num1[::-1]
    num2 = num2[::-1]

    app = abs(len(num1) - len(num2))
    if len(num1) > len(num2):
        num2 = num2 + ("0" * app)
    else:
        num1 = num1 + ("0" * app)

    diff = ""

    for i in range(len(num1)):
        if num1[i] < num2[i]:
            for j in range(i + 1, len(num1)):
                if num1[j] != "0":
                    num1 = num1[:j] + str(int(num1[j]) - 1) + num1[j + 1 :]
                    diff = diff + str((10 + int(num1[i])) - int(num2[i]))
                    break
                else:
                    x = 1
                    for k in range(j + 1, len(num1)):
                        if num1[k] != "0":
                            num1 = num1[:j] + "9" * x + num1[k:]
                            num1 = num1[:k] + str(int(num1[k]) - 1) + num1[k + 1 :]
                            break
                        x += 1
                    diff = diff + str((10 + int(num1[i])) - int(num2[i]))
                    break
        else:
            diff = diff + str(int(num1[i]) - int(num2[i]))

    if len(a) < len(b):
        return "-" + diff[::-1]
    if (len(a) == len(b)) and (a < b):
        return "-" + diff[::-1]

    return diff[::-1]


print(SumNegativeOnly("-1", "1"))
