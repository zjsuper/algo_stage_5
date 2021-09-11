class Solution:
    def romanToInt(self, s: str) -> int:
        dicroma = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0
        for i in range(len(s)-1):
            if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                num -=  dicroma[s[i]]
            elif s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                num -=  dicroma[s[i]]
            elif s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                num -=  dicroma[s[i]]
            else:
                num += dicroma[s[i]]
        num += dicroma[s[-1]]
        return num