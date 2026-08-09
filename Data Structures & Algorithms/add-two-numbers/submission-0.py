# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head

        carry = 0
        while l1 or l2:
            digit1 = 0
            digit2 = 0
            if l1: digit1 = l1.val
            if l2: digit2 = l2.val
            mysum = digit1+digit2+carry
            carry = mysum // 10
            curr.next = ListNode(mysum % 10)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry == 1:
            curr.next = ListNode(1)
        
        return head.next