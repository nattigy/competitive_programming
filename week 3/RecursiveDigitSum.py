def superDigit(n, k):
    length = len(n)
    if length == 0:
        return 0
    if length == 1:
        return int(n)
    summ = 0
    for num in n:
        summ += int(num)
    return superDigit(str(summ * k), 1)
