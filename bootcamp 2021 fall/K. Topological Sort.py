from collections import defaultdict

def topologicalSort(nodes, remove_nodes):
    indegree = defaultdict(int)
    graph = defaultdict(set)
    for g in nodes:
        indegree[g[0]] = indegree.get(g[0],0)
        indegree[g[1]] = indegree.get(g[0],0)+1
        graph[g[0]].add(g[1])
    for r in remove_nodes:
        if r in nodes:
            indegree[r[1]] -= 1
            graph[r[0]].remove(r[1])
    queue = []
    for key in indegree:
        if indegree[key] == 0:
            queue.append(key)
    print_nodes = ""
    while queue:
        pop = queue.pop()
        print_nodes += str(pop) + " "
        for n in graph[pop]:
            indegree[n] -= 1
            if indegree[n] == 0:
                queue.append(n)
    return print_nodes

test_cases = int(input())
result = []
for _ in range(test_cases):
    (num_nodes, remove) = input().split(" ")
    remove_node = []
    node = []
    for i in range(1, int(num_nodes)+1):
        for j in range(i+1, int(num_nodes)+1):
            node.append([i, j])
    for n in range(int(remove)):
        (left, right) = input().split(" ")
        remove_node.append([int(left), int(right)])
    result.append(topologicalSort(node, remove_node))
print("\n".join(result))