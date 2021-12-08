from collections import defaultdict, deque

def party(emp):
    graph = defaultdict(list)
    queue = deque([])
    for i in range(len(emp)):
        if emp[i] != -1:
            graph[emp[i]].append(i + 1)
        else:
            queue.append(i + 1)

    groups = 0
    while queue:
        length = len(queue)
        for i in range(length):
            pop = queue.popleft()
            for e in graph[pop]:
                queue.append(e)
        groups += 1

    return groups

num = int(input())
emp = []
for _ in range(num):
    em = int(input())
    emp.append(em)
    
print(party(emp))