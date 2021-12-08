def gamerHemose(weapons, health):
    length = len(weapons)
    weapons.sort()
    max_1 = weapons[-1]
    max_2 = weapons[length - 2]
    if health <= max_1:
        return 1
    sm = max_1 + max_2
    mod = health % sm
    if mod == 0:
        return 2 * (health//sm)
    if mod <= max_1:
        return (2 * (health//sm)) + 1
    return 2 * (health//sm) + 2

tests = int(input())
ans = []
for _ in range(tests):
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    ans.append(str(gamerHemose(second, first[1])))
    
print("\n".join(ans))