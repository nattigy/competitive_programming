from collections import defaultdict


def hierarchy(num, qual, apps):
    count = 0
    hie_map = defaultdict(int) #hierarchy
    for a in apps:
        if hie_map.get(a[1], -1) < 0:
            hie_map[a[1]] = a[2]
            count += a[2]
        elif hie_map[a[1]] > a[2]:
            count -= hie_map[a[1]]
            hie_map[a[1]] = a[2]
            count += a[2]
            
    if len(hie_map) == num - 1:
        return count
    return -1

n = int(input()) #employees
q = list(map(int, input().split())) #qualifications
a = int(input()) # number applications
m = [] #applications with their cost
for _ in range(a):
    m.append(list(map(int, input().split())))
    
print(hierarchy(n, q, m))