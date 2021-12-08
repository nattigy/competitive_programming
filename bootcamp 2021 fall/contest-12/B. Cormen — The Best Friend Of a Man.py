def cormenTheBestFriendOfAMan(n, days, k):
    if n == 1:
        print(0)
        print(days[0])
        return
    i = 0
    j = 1
    dist = 0
    while j < n:
        left = k - (days[i] + days[j])
        if left > 0:
            dist += left
            days[j] += left
        j += 1
        i += 1
        
    print(dist)
    print(*days)

n, d = list(map(int, input().split()))
days = list(map(int, input().split()))
cormenTheBestFriendOfAMan(n, days, d)