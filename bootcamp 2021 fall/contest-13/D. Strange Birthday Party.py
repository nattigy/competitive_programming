def strangeBirthdayParty(friends, gifts):
    friends = sorted(friends)
    length = len(gifts)
    cost = 0
    g = 0
    for i in range(len(friends) - 1, -1 , -1):
        if g <= friends[i] - 1:
            if gifts[g][1] == 0:
                cost += gifts[g][0]
                g += 1
        else:
            cost += gifts[friends[i] - 1][0]
        if g >= length:
            g -= 1
    return cost

tests = int(input())
ans = []
for _ in range(tests):
    n, m = list(map(int, input().split()))
    friends = list(map(int, input().split()))
    gifts = list(map(int, input().split()))
    ans.append(strangeBirthdayParty(friends, [[i, 0] for i in gifts]))
print(*ans, sep="\n")