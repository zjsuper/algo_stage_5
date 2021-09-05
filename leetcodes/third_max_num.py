class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        list3 = [-float(inf)]*3
        print(nums)
        for m in nums:
            if m > list3[0]:
                list3[2] = list3[1] 
                list3[1] = list3[0]
                list3[0] = m
            if m < list3[0] and m > list3[1]:
                list3[2] = list3[1] 
                list3[1] = m
                print(m,'second if')
            if m < list3[1] and m > list3[2]:
                list3[2] = m
        print(list3)
        if list3[2] > -float(inf):
            return list3[2]
        else:
            return list3[0]