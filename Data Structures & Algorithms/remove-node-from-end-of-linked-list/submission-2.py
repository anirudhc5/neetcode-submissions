# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for _ in range(n+1):
            # advance fast n+1 times
            fast = fast.next
            
        while fast is not None:
            # increment both pointers by one until fast is at the end of the list
            # slow will be at the n+1th from the tail
            slow = slow.next
            fast = fast.next

        # remove the nth node from the end
        slow.next = slow.next.next

        # return the head of the list
        return dummy.next
