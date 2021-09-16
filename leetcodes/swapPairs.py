def swapPairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None:
            return None
        elif head.next == None:
            return head
        else:
            cur = head
            prev = ListNode(0)
            prev.next = cur
            while prev.next and prev.next.next:
                cur = prev.next
                nextn = cur.next
                cur.next = nextn.next
                nextn.next = cur
                prev.next = nextn
            return prev.next
                