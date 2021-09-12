class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #123000, 256
        x = 0
        if m == 0:
            for i in range(n):
                nums1.insert(i,nums2[i])
                nums1.pop()
                
                
        else:
            for i in nums2:
            #print(i)
                for j in range(m-1+x,-1,-1):
                #print(i,nums1[j])
                    if i >= nums1[j]:
                    #print(j)
                    #print('kaishi',i)
                        nums1.insert(j+1,i)
                    #print(nums1)
                        nums1.pop()
                    #print(nums1)
                        x += 1
                        break
                    if j ==0:
                        nums1.insert(0,i)
                        nums1.pop()
                        x += 1