def redBlue(red, blue):
    if int(red) == int(blue):
        return "EQUAL"
    red_count = 0
    blue_count = 0
    for i in range(len(red)):
        if int(red[i]) < int(blue[i]):
            blue_count += 1
        elif int(red[i]) > int(blue[i]):
            red_count += 1
        
    if red_count > blue_count:
        return "RED"
    elif red_count < blue_count:
        return "BLUE"
    else:
        return "EQUAL"

test = int(input())
ans = []
for _ in range(test):
    nn = input()
    red = input()
    blue = input()
    ans.append(redBlue(red, blue))
for a in ans:
    print(a)
    