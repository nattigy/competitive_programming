def redAndBlue(red, blue):
    big = [0, 0]
    for i, array in enumerate([red, blue]):
        summ = 0
        for j in array:
            summ += j
            big[i] = max(big[i], summ)
    return sum(big)

tests = int(input())
ans = []
for _ in range(tests):
    _, red = input(), list(map(int, input().split()))
    _, blue = input(), list(map(int, input().split()))
    ans.append(str(redAndBlue(red, blue)))
print("\n".join(ans))
