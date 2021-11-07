def makeItDividible(num):
    count = 0
    minn = 0
    if num % 25 == 0:
        return count
    arr = recursion(str(num))
# def makeItDividible(num):
#     count = 0
#     if num % 25 == 0:
#         return count
#     snum = str(num)
#     for i in range(len(snum)-1,0,-1):
#         if int(snum[i]) == 0 and (int(snum[i-1]) == 0 or int(snum[i-1]) == 5):
#             if i == len(snum)-1:
#                 return 0
#             return count + len(snum[i+1:])
#         if int(snum[i]) % 5 != 0 and int(snum[i]) != 0:
#             snum = snum[:i]+snum[i+1:]
#             count += 1
#             i += 1
#             if int(snum)%25==0:
#                 return count
#     return count


print(makeItDividible(700013405))
if __name__ == "__main__":
    length_of_input = input().rstrip().split()
    num = length_of_input[0]
    l = length_of_input[1]
    r = length_of_input[2]
    # print(CodeFor1(num, l, r))