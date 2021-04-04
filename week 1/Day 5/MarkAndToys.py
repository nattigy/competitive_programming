def MarkAndToys(prices, k):
    # smallest = 0
    summ = 0
    res = 0
    prices.sort()

    for price in prices:
        if summ + price <= k:
            summ += price
            res += 1
        else:
            return res
    return res


print(MarkAndToys([1, 12, 5, 111, 200, 1000, 10], 50))
