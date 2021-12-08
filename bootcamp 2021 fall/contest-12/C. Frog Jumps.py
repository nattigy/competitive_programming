def frogJumps(chars):
    length = len(chars)
    j = 1
    maxx = 0
    count = 0
    while j < length:
        if chars[j] == "L":
            count += 1
            maxx = max(count, maxx)
        else:
            count = 0
        j += 1
    return maxx + 1

tests = int(input())
ans = []
for _ in range(tests):
    inp = input()
    chars = ["s"]
    for c in inp:
        chars.append(c)
    chars.append("e")
    ans.append(frogJumps(chars))
print(*ans, sep="\n")