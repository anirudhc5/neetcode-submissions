# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = ListNode(next=head)
        ptr = ans.next

        length = 0
        while ptr:
            length += 1
            ptr = ptr.next
        
        i = 0
        goal = length - n + 1
        ptr = ans
        while i < goal - 1:
            ptr = ptr.next
            # print(ptr.val)
            i += 1
        if ptr.next:
            ptr.next = ptr.next.next
        return ans.next
