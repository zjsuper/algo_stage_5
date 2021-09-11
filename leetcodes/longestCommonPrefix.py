class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #find shortest str then iterate
        strlens = [len(i) for i in strs]
        mins = min(strlens)
        # shortidx = 0
        # for n,i in enumerate(strlens):
        #     if i == mins:
        #         shortidx = n
        
        for m in range(mins):
            temp = strs[0][0:m+1]
            for k in strs:
                if k[0:m+1]!=temp:
                    return strs[0][0:m]
        return strs[0][0:mins]