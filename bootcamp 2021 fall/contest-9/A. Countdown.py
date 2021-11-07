def countDown(n, num):
    count = 0
    for i in range(len(num)):
        count += int(num[i])
        if i < n - 1 and num[i] != '0':
            count += 1
    return count

test = int(input())
ans = []
for _ in range(test):
    length = int(input())
    number = input()
    ans.append(countDown(length, number))

for a in ans:
    print(a)