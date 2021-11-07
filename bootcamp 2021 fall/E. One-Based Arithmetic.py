def oneBased(num):
    return recursion(num)

def recursion(num):
    if num <= 6:
        return num
    if num > 6 and num <= 11:
        return 2 + 11 - num
    length = len(str(num))
    new_num = '1'*(length)
    last_num = '9'*(length)
    if num > (int(last_num)+1)//2:
        next_num = int('1'*(length+1))
        summ = length+1
        mul = ((next_num-num)//int(new_num))-1
        return summ + mul + recursion(abs(int(next_num)-(mul*int(new_num)+num)))
    else:
        return length + recursion(abs(num-int(new_num)))

n = input()
print(oneBased(int(n)))