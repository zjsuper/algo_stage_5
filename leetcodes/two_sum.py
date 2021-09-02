class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i,num in enumerate(nums):
            remain = target -num
            if remain in visited:
                return [i,visited[remain]]
            else:
                visited[num] = i