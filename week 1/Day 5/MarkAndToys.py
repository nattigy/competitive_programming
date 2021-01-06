def MarkAndToys(prices, k):
    smallest = 0
    summ = 0
    res = 0
    for i in range(len(prices)):
        smallest = prices[i]
        for j in range(i + 1, len(prices)):
            if prices[j] < smallest:
                smallest = prices[j]
                prices[i], prices[j] = prices[j], prices[i]

        if summ + prices[i] <= k:
            summ += prices[i]
            res += 1
        else:
            break

    return res


print(MarkAndToys([1, 12, 5, 111, 200, 1000, 10], 50))
