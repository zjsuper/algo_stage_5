```
给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

示例 1:

输入: S = "loveleetcode", C = 'e'
输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
说明:

- 字符串 S 的长度范围为 [1, 10000]。
- C 是一个单字符，且保证是字符串 S 里的字符。
- S 和 C 中的所有字母均为小写字母。


idea: iterate the string, use dictionary to save the distance and update

时间复杂度：O(N*K)O(N∗K)，N 是 S 的长度，K 是字符 C 在字符串中出现的次数，K <= NK<=N。

空间复杂度：O(K)O(K)，K 为字符 C 出现的次数，这是记录字符 C 出现下标的辅助数组消耗的空间。
```
#idea: iterate the string, use dictionary to save the distance and update
class Solution:
	def shortestToChar(self, s: str, c: str) -> List[int]:
		dic = {c:[]}
		lens = len(s)
		output = []
		for i in range(lens):
			if s[i] == c:
				dic[c].append(i)
		for i in range(lens):
			temp = [abs(i-k) for k in dic[c]]
			output.append(min(temp))
		return output


##improve:

class Solution:
	def shortestToChar(self, s: str, c: str) -> List[int]:
		dic = {c:[]}
		lens = len(s)
		dic_s = {i:100000000 for i in range(lens)}
		output = []
		for i in range(lens):
			if s[i] == c:
				dic[c].append(i)
		for i in range(lens):
			for j in dic[c]:
					temp = abs(j-i)
					if temp < dic_s[i]:
						dic_s[i] = temp
					else:
						pass
			output.append(dic_s[i])

		return output


###improve 双指针