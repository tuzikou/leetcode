class Solution:
    def reverse(self, x):
        temp =  str(x)[::-1]
        maxnum = 2**31
        if temp[-1] == '-' and int(temp[:-1])<maxnum:
            return -int(temp[:-1])
        elif temp[-1] != '-' and int(temp)<maxnum-1:
            return int(temp)
        else:
            return 0
            
#注意负数和反转后超出int范围的数
