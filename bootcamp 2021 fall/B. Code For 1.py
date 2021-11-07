def CodeFor1(num, i, j):
    result = CodeFor1Recursion(num)
    result = result[i:j+1]
    count = 0
    for i in result:
        if i == 1:
            count += 1
    return count
def CodeFor1Recursion(num):
    if num <= 1:
        return [num]
    result = [num//2, num%2, num//2]
    response = []
    for r in result:
        val = CodeFor1Recursion(r)
        for v in val:
            response.append(v)
    return response


length_of_input = input().rstrip().split()
num = length_of_input[0]
l = length_of_input[1]
r = length_of_input[2]
print(CodeFor1(int(num), int(l), int(r)))