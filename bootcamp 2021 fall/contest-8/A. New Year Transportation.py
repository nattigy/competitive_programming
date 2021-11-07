def newYearTransportation(num_cells, dest, portals):
    if dest == 1:
        return "YES"
    i = 1
    while i < num_cells:
        i = i+portals[i-1]
        if dest == i:
            return "YES"
    return "NO"


first = input().rstrip().split(" ")
num_cells = int(first[0])
dest = int(first[1])
second = input().rstrip().split(" ")
portals = []
for s in second:
    portals.append(int(s))
print(newYearTransportation(num_cells, dest, portals))