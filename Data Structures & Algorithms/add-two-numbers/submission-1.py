# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        curr = ans

        carry = 0
        while l1 or l2:
            l1digit = 0
            l2digit = 0
            if l1: l1digit = l1.val
            if l2: l2digit = l2.val
            total = l1digit + l2digit + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry == 1:
            curr.next = ListNode(1)

        return ans.next
        