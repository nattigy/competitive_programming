def climbingLeaderboard(ranked, player):
    res = []
    nr = []
    for i in range(len(ranked)):
        if i == 0:
            nr.append(ranked[i])
        elif ranked[i] != ranked[i - 1]:
            nr.append(ranked[i])

    # [100, 50, 40, 20, 10]
    for i in range(len(player)):
        for j in range(len(nr)):
            if nr[j] <= player[i]:
                res.append(j + 1)
                break
            if j + 1 == len(nr):
                res.append(len(nr) + 1)
                break
    return res


print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
