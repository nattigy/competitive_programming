def letters(rooms, messages):
    prefix = []
    summ = 0
    for r in rooms:
        summ += r
        prefix.append(summ)

    i = 0
    j = 0
    while j < len(messages) and i < len(prefix):
        if messages[j] <= prefix[i]:
            if i == 0:
                print(i + 1, messages[j])
            else:
                print(i + 1, messages[j] - prefix[i - 1])
            j += 1
        else:
            i += 1


n, m = input().split(" ")
second = input().split(" ")
rooms = []
for s in second:
    rooms.append(int(s))
third = input().split(" ")
messages = []
for t in third:
    messages.append(int(t))

letters(rooms, messages)
