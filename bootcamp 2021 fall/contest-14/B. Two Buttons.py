from collections import deque

def twoButtons(n, m):
    count = 0
    if n == m:
        return count
    queue = deque([n])
    visited = set()
    while queue:
        length = len(queue)
        for i in range(length):
            pop = queue.popleft()
            visited.add(pop)
            if pop == m:
                return count
            if pop*2 not in visited:
                queue.append(pop*2)
            if pop-1 not in visited and pop-1 > 0:
                queue.append(pop-1)
        count += 1
    return count

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    print(twoButtons(n, m))