def updateFiles(c, k):
    updated = 1
    time = 0
    while updated < c:
        if updated <= k:
            updated += updated
        elif updated > k:
            un_updated = c - updated
            if un_updated % k == 0:
                return time + un_updated // k
            else:
                return time + (un_updated // k) + 1
        time += 1
    return time

tests = int(input())
ans = []
for _ in range(tests):
    [c, k] = input().split(" ")
    ans.append(updateFiles(int(c), int(k)))
for a in ans:
    print(a)