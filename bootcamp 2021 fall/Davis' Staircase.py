from functools import cache
#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def stepPerms(n):
    # Write your code here
    return recursion(n-1)+recursion(n-2)+recursion(n-3)
@cache
def recursion(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return recursion(n-1)+recursion(n-2)+recursion(n-3)