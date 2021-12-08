from collections import deque

def foxAndNames(names):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    queue = deque([])
    indegree = {}
    graph = {}
    for name in names:
        pass
    for a in alphabet:
        if a not in queue:
            result += a
            continue
        if queue:
            if queue[0] == a:
                pop = queue.popleft()
                result += pop
                i = 0
                while queue:
                    if queue[0] > pop:
                        break
                    top = queue.popleft()
                    if top != result[-1]:
                        result += top
                    i += 1
    return result

tests = int(input())
array = []
for _ in range(tests):
    array.append(input())
print(foxAndNames(array))