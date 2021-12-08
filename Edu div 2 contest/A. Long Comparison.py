def longComparison(n, z1, m, z2):
    if n > m and z1 > z2:
        return ">"
    if n < m and z1 < z2:
        return "<"
    if n == m and z1 == z2:
        return "="
    
    diff  = abs(z1-z2)
    if diff > 0:
        n *= 10*int("1"+"0"*diff)
        m *= 10*int("1"+"0"*diff)
    else:
        if n == m:
            return "="
        if n > m:
            return ">"
        return "<"
    

tests = int(input())
ans = []
for _ in range(tests):
    n, z1 = list(map(int, input().split()))
    m, z2 = list(map(int, input().split()))
    ans.append(longComparison(n, z1, m, z2))
print(*ans, sep="\n")