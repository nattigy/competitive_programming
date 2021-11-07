def combinatoricsHomework(letters, m):
    if m == 0:
        return "YES"
    count = 0
    for l in letters:
        if l > 1:
            count += l // 2
    if count == m:
        return "YES"
    return "NO"

tests = int(input())
ans = []
for _ in range(tests):
    second = input().rstrip().split(" ")
    ans.append(combinatoricsHomework([int(second[0]), int(second[1]), int(second[2])], int(second[3])))
for a in ans:
    print(a)