def pairOfTopics(t, s, n):
    count = 0
    diff = []
    for i in range(n):
        diff.append(t[i] - s[i])
    diff.sort()
    i = 0
    j = n - 1
    while i < j:
        if diff[i] + diff[j] > 0:
            count += j - i
            j -= 1
        else:
            i += 1
    return count

n = int(input())
t = list(map(int, input().split()))
s = list(map(int, input().split()))
print(pairOfTopics(t, s, n))