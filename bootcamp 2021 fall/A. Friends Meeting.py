def friendsMeeting(a, b):
    diff = abs(a - b)
    if diff == 1:
        return 1
    
    xa = diff // 2
    xb = diff - xa
    
    return doSum(xa) + doSum(xb)

def doSum(n):
    return n * (n + 1) // 2

a, b = int(input()), int(input())
print(friendsMeeting(a, b))