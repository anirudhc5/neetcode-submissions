# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0, None)
        ptr = ans

        while list1 and list2:
            # print(list1.val, list2.val)
            if list1.val < list2.val:
                ptr.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                ptr.next = ListNode(list2.val, None)
                list2 = list2.next
            ptr = ptr.next
        if list1:
            ptr.next = list1
        else:
            ptr.next = list2
        return ans.next
        