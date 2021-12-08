def joysticks(a, b):
    time = 0
    while a > 0 and b > 0:
        if a > b:
            a, b = b, a
        a += 1
        b -= 2
        if a < 0 or b < 0:
            break
        time += 1
    return time

a, b = list(map(int, input().split()))
print(joysticks(a, b))