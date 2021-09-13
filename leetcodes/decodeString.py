
#idea all strings are sperate by the num[], find each subpart string then merge
Class Solution:
    def decodeString(self, s:str) -> str:
        stack = []
        strs,nums = '',''
        for i in s:
            if i.isdigit():
                nums += i
            elif i.isalpha():
                strs += i
            elif i == '[':
                stack.append((strs,int(nums)))
                strs,nums = '',''
            elif i == ']':
                prev,num = stack.pop()
                strs = prev+num*strs
        return a