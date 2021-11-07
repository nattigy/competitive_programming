def ComplicatedGCD(num1, num2):
    if num1 == num2:
        return int(num2)
    return 1
    
inp = input().split(" ")
print(ComplicatedGCD(inp[0], inp[1]))