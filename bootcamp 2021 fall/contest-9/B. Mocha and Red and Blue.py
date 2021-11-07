from collections import deque 

def mochaAndRedAndBlue(colors):
    length = len(colors)
    dir = [-1, 1]
    queue = deque([])

    for i in range(length):
        if colors[i] != "?":
            queue.append(i)
    if not queue:
        queue.append(0)
        colors[0] = "R"

    while queue:
        pop = queue.popleft()
        for d in dir:
            if pop + d < length and pop + d >= 0:
                if colors[pop + d] == "?":
                    colors[pop + d] = "B" if colors[pop] == "R" else "R"
                    queue.append(pop + d)

    return "".join(colors)


test = int(input())
ans = []
for _ in range(test):
    n = input()
    colors = input()
    arr = []
    for c in colors:
        arr.append(c)
    ans.append(mochaAndRedAndBlue(arr))
for a in ans:
    print(a)
