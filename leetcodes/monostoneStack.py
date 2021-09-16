class Solution:
    def monostoneStack(self, T):
        stack = []
        ans = [0] * len(T)
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                peek = stack.pop(-1)
                ans[peek] = i - peek
            stack.append(i)
        return ans

"""
注意这里的栈仍然是非空的，如果有的题目需要用到所有数组的信息，那么很有可能因没有考虑边界而不能通过所有的测试用例。 这里介绍一个技巧 - 哨兵法，这个技巧经常用在单调栈的算法中。

对于上面的例子，我可以在原数组 [1,3,4,5,2,9,6] 的右侧添加一个小于数组中最小值的项即可，比如 -1。此时的数组是 [1,3,4,5,2,9,6,-1]。这种技巧可以简化代码逻辑，大家尽量掌握。

上面的例子如果你明白了，就不难理解为啥单调栈适合求解下一个大于 xxx或者下一个小于 xxx这种题目了。比如上面的例子，我们就可以很容易地求出在其之后第一个小于其本身的位置。比如 3 的索引是 1，小于 3 的第一个索引是 4，2 的索引 4，小于 2 的第一个索引是 0，但是其在 2 的索引 4 之后，因此不符合条件，也就是不存在在 2 之后第一个小于 2 本身的位置。

上面的例子，我们在第 6 步开始 pop，第一个被 pop 出来的是 5，因此 5 之后的第一个小于 5 的索引就是 4。同理被 pop 出来的 3，4，5 也都是 4。

如果用 ans 来表示在其之后第一个小于其本身的位置，ans[i] 表示 arr[i] 之后第一个小于 arr[i] 的位置， ans[i] 为 -1 表示这样的位置不存在，比如前文提到的 2。那么此时的 ans 是 [-1,4,4,4,-1,-1,-1]。

第 8 步，我们又开始 pop 了。此时 pop 出来的是 9，因此 9 之后第一个小于 9 的索引就是 6。

这个算法的过程用一句话总结就是，如果压栈之后仍然可以保持单调性，那么直接压。否则先弹出栈的元素，直到压入之后可以保持单调性。
这个算法的原理用一句话总结就是，被弹出的元素都是大于当前元素的，并且由于栈是单调减的，因此在其之后小于其本身的最近的就是当前元素了
"""
def monostoneStack(T):
    stack = []
    ans = [0] * len(T)
    for i in range(len(T)):
        while stack and T[i] > T[stack[-1]]:
            print('round',i)
            print(i,T[i],T[stack[-1]])
            peek = stack.pop(-1)
            ans[peek] = i - peek
            print(peek,ans[peek])
        stack.append(i)
        #print(i,T[i],stack[-1],T[stack[-1]])
    return ans



ans = monostoneStack([1,3,4,5,2,9,6])


print(ans)