import heapq

def eugenyAndPlayList(durations, moments):
    heap = []
    summ = 0
    for i in range(len(durations)):
        prev = summ + 1
        summ += durations[i]
        heapq.heappush(heap, (prev, summ, i+1))
    for m in moments:
        while heap:
            pop = heapq.heappop(heap)
            if pop[0] <= m and m <= pop[1]:
                print(pop[2])
                heapq.heappush(heap, pop)
                break

num_songs = int(input().split(" ")[0])
durations = []
for _ in range(num_songs):
    [c,t] = input().split(" ")
    durations.append(int(c)*int(t))
moments_input = input().split(" ")
moments = []
for m in moments_input:
    moments.append(int(m))

eugenyAndPlayList(durations, moments)