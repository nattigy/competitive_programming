from collections import defaultdict
from typing import DefaultDict

def top(n,graph,indegree, k):
    if k>=n:
        return 0
    first = []
    second = []
    for key,item in indegree.items():
        if item == 1:
            first.append(key)
    op=0
    nodes=0
    while op < k and first:
        nodes += len(first)
        for cur in first:
            for nbr in graph[cur]:
                indegree[nbr] -= 1
                if indegree[nbr] == 1:
                    second.append(nbr)
        op+=1
        first = second
        second = []
    return n-nodes

test = int(input())
ans=[]
for _ in range(test):
    x=input()
    [n,k] = input().split(" ")
    n = int(n)
    k = int(k)
    indegree = defaultdict(int)
    graph= defaultdict(list)
    for _ in range(n-1):
        pair = input()
        [lft,right]= pair.split(" ")
        lft = int(lft)
        right = int(right)
        graph[lft].append(right)
        graph[right].append(lft)
        indegree[lft]+=1
        indegree[right]+=1
    leaf=0
    for i in range(n):
        if i+1 not in graph:
            leaf+=1
    ans.append(top(n-leaf, graph, indegree, k))
for x in ans:
    print(x)