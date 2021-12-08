def teamComposition(a, b):
    if (a + b) < 4:
        return 0
    if a == 0 or b == 0:
        return 0     
    if a == b:
        return (a + b) // 4
    
    if a > b:
        a, b = b, a
    
    return min((b + a)//4, a)

tests = int(input())
ans = []
for _ in range(tests):
    a, b = list(map(int, input().split()))
    ans.append(teamComposition(a, b))
print(*ans, sep="\n")