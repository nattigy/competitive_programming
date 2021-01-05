class Solution(object):
    def reverse(self, x):
        y=abs(x)
        z = 0
        while(y!=0):
            n = y%10
            z += n
            z *= 10
            y = (y-n)//10
        z = z//10 if x > 0 else -1*z//10
        if (pow(-2,31) <= z <= pow(2,31) - 1):
            return z
        return 0

