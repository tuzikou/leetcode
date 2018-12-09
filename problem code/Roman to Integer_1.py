class Solution:
    def romanToInt(self, s):
        ts = s + ' ' 
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,' ':0}
        re,temp = 0,0
        for i in range(len(s)):
            if dic[ts[i]]==dic[ts[i+1]]:
                temp += dic[ts[i]]
            elif dic[ts[i]]<dic[ts[i+1]]:
                temp -= dic[ts[i]]
            else:
                re += temp+dic[ts[i]]
                temp = 0
        return re+temp
#太慢了
