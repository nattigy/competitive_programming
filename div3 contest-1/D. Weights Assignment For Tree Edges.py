def weightsAssignmentForTreeEdges(tree, dist):
    pass

tests = int(input())
ans = []
for _ in range(tests):
    tree = list(map(int, input().split()))
    dist = list(map(int, input().split()))
    ans.append(weightsAssignmentForTreeEdges(tree, dist))

for a in ans:
    print(*a)