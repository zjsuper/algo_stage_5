
#idea: two iterations to add and decompose the num
# time and space o(N)

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        nums = 0
        length = len(num)
        
        for i in range(length):
            nums += num[i] * (10**(length-1-i))
        print(nums)
        nums2= nums+k
        list1 = []
        if nums2 == 0:
            return[0]
        while nums2:
            a= nums2%10
            nums2 //= 10
            list1.insert(0,a)
        return list1

思路
从数组末尾开始往前遍历，每一位先和 k 相加。
相加的和 %10 就是这一位应有的数值，相加的和 整除10 就是下一位的 k 。

注意：如果数组遍历结束后， k 仍然不为 0 ，那么需要将剩下的 k 加入到数组开头








class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        #iteration from end to begin:
        len_ori = len(num)
        for i in range(len(num)-1,-1,-1):
            k_last = k % 10
            k //= 10
            temp = num[i] + k_last
            if temp>= 10:
                last_digit = temp % 10
                if i-1>=0:
                    num[i-1] += 1
                    num[i] = last_digit
                else:
                    num[i] = last_digit
                    num.insert(0,1)
            else:
                num[i] = temp
        if len(num) != len_ori and k > 0:
            k_last = k % 10
            k //= 10
            temp = num[0] + k_last
            if temp>= 10:    
                last_digit = temp % 10      
                num[0] = last_digit
                num.insert(0,1)
            else:
                num[0] = temp
            while k:
                k_last = k % 10
                k //= 10
                num.insert(0,k_last)
        elif len(num) == len_ori and k > 0:
            while k:
                k_last = k % 10
                k //= 10
                num.insert(0,k_last)
        return num


#improve: 时间空间复杂度都为n
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        len_ori = len(num)
        for i in range(len(num)-1,-1,-1):
            k_last = k % 10
            k //= 10
            temp = num[i] + k_last
            if temp>= 10:
                last_digit = temp % 10
                if i-1>=0:
                    num[i-1] += 1
                    num[i] = last_digit
                else:
                    num[i] = last_digit
                    num.insert(0,1)
            else:
                num[i] = temp
        if len(num) != len_ori and k > 0:
            k_last = k % 10
            k //= 10
            temp = num[0] + k_last
            if temp>= 10:    
                last_digit = temp % 10      
                num[0] = last_digit
                num.insert(0,1)
                adddigit = True
            else:
                num[0] = temp
                adddigit = False
            while k:
                k_last = k % 10
                k //= 10
                if adddigit:
                    temp = num[0] + k_last
                    if temp>= 10:   
                        last_digit = temp % 10      
                        num[0] = last_digit
                        num.insert(0,1)
                        adddigit = True  
                    else: 
                        num[0] = temp              
                        
                        adddigit = False
                else:
                    num.insert(0,k_last)
        elif len(num) == len_ori and k > 0:
            while k:
                k_last = k % 10
                k //= 10
                num.insert(0,k_last)
        return num













class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num)-1, -1, -1):
            k_add_num = num[i] + k
            num[i] = k_add_num % 10
            k = k_add_num // 10
            # 提前退出循环的trick
            if not k:
                break
        
        if k:
            while k:
                num.insert(0, k % 10)
                k = k // 10
        
        return num