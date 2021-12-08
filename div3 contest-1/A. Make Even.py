def makeEven(num):
    if len(num) == 1:
        return 0 if int(num) % 2 == 0 else -1
    
    if int(num[-1]) % 2 == 0:
        return 0
    
    if int(num[0]) % 2 == 0:
        return 1
    
    for n in num:
        if int(n) % 2 == 0:
            return 2
    return -1

tests = int(input())
ans = []
for _ in range(tests):
    ans.append(makeEven(input()))
print(*ans, sep="\n")