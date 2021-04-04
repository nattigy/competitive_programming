def CountingValleys(s, p):
    # s steps
    # p path

    res = 0
    summ = 0

    for i in p:
        if i == "U":
            res += 1
        if i == "D":
            res -= 1
        if i == "U" and res == 0:
            summ += 1

    return summ


print(CountingValleys(6, "UDDDUDUU"))