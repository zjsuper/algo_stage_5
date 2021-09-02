class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        a = abs(x)
        digit_list = []
        while a != 0:
            lastd = a%10
            a = (a - lastd)/10
            digit_list.append(lastd)
        while digit_list[0] == 0:
            digit_list.pop(0)
        lens = len(digit_list)
        num = 0
        for i in digit_list:
            num += i*10**(lens-1)
            lens = lens-1
        if x <0 and num <= 2**31:
            return -int(num)
        if x >0 and num <= (2**31-1):
            return int(num)
        else:
            return 0
        
        
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        a = abs(x)
        # if x > 0:
        #     sym = 1
        # else:
        #     sym = -1
        num  = 0
        while a:
            ld = a % 10
            a //= 10
            num = num*10 + ld
        
        if x <0 and num <= 2**31:
            return -int(num)
        if x >0 and num <= (2**31-1):
            return int(num)
        else:
            return 0