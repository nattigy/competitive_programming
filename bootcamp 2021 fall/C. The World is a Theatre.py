def worldTheatre(n, m, t):
    combinations = []
    for i in range(4, t):
        if 1 <= t - i <= m and 1 <= i <= n:
            combinations.append([i,t-i])
    result = 0
    for c in combinations:
        b = c[0]
        g = c[1]
        result += doFactorial(n, m, b, g)
    return int(result//1)

def doFactorial(n, m, b, g):
    return (factorial(n)//(factorial(b)*factorial(n-b)))*(factorial(m)//(factorial(g)*factorial(m-g)))

def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    res = 1
    for i in range(n, 1, -1):
        res *= i
    return res

[n, m, t] = input().split(" ")
print(worldTheatre(int(n), int(m), int(t)))