from collections import defaultdict, deque

def reposts(chain):
    graph = defaultdict(list)
    # visited = set()
    for c in chain:
        graph[c[0]].append(c[1])
    queue = deque([])
    queue.append(graph['polycarp'])
    # visited.add('polycarp')
    count = 0
    while queue:
        length = len(queue)
        for i in range(length):
            pop = queue.popleft()
            for j in range(len(pop)):
                # if pop[j] not in visited:
                queue.append(graph[pop[j]])
                    # visited.add(pop[j])
        count += 1
    return count
            

first = int(input())
chain = []
for _ in range(first):
    post = input().rstrip().split(" ")
    chain.append([post[2].lower(), post[0].lower()])
print(reposts(chain))