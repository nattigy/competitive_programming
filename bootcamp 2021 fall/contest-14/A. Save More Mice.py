def saveMoreMice(hole, places):
    places.sort()
    places.reverse()
    length = len(places)
    prefix = []
    count = 0
    saved = 0
    for i in range(length):
        count += (hole - places[i])
        prefix.append(count)
        if prefix[i] < hole:
            saved += 1
        else:
            break
    return saved


if __name__ == "__main__":
    tests = int(input())
    ans = []
    for _ in range(tests):
        h, k = list(map(int, input().split()))
        places = list(map(int, input().split()))
        ans.append(saveMoreMice(h, places))
    print(*ans, sep="\n")