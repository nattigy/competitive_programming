def ATMAndStudents(students, money):
    length = len(students)
    maxx = 0
    res = [-1]
    count = money
    i = 0
    j = 0
    while j < length and i < length:
        count += students[j]
        if count >= 0 and maxx < (j - i + 1):
            maxx = j - i + 1
            res = [i + 1, j + 1]
        if count < 0:
            count -= students[i]
            i += 1
        if count >= 0:
            j += 1
        else:
            count -= students[j]
    return res

tests = int(input())
ans = []
for _ in range(tests):
    a, b = list(map(int, input().split()))
    students = list(map(int, input().split()))
    ans.append(ATMAndStudents(students, b))
for a in ans:
    print(*a)