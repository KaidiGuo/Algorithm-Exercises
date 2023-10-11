# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
if one of the list is empty, return the other

create a dummy node and a moving cur pointer
when both l1,l2 nodes exist, compare their value, let the cur.next point to the smaller one,
move only the smaller one's pointer to its next (because this smaller value is used, the bigger value is not),
move cur to its next, loop

when one of l2,l2 reaches its end, let the cur.next be the rest of l1 or l2
return dummy.next

this is a inplace method, we could of cause choose to create a new linked list using sorted values
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        if not l1 and not l2:
            return l1 or l2
        while l1 and l2:
            if l1.val< l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
    
    
    
    
