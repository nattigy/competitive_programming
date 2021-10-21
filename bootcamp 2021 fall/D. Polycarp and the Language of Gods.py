def polycarp(word):
    prev = True
    count = 0
    for w in word:
        if w == 'w':
            count += 1
            prev = True
        elif w == 'v' and not prev:
            count += 1
            prev = True
        else:
            prev = False
    return count

length_of_input = eval(input())
for l in range(length_of_input):
    word = input()
    print(polycarp(word))