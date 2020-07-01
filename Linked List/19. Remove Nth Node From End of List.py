# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
one pass method:
use two pointer, with a gap length = n
move them together until the faster one reach the end of the list
thus, the slower one will point to the one node just before our need-to-remove node
set its next ot its next next. done.

and if the fast node does not exist, meaning the to be deleted node is the first node, just return head.next
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast=slow=head
        while n:
            fast=fast.next
            n-=1
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head