class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = x
        if x < 0 :
            return False
        else:
            num = 0
            while x:
                last_d = x%10
                x //= 10
                num = num*10 + last_d
            if num == a:
                return True
            else:
                return False