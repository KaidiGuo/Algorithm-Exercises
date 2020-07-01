# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Math
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = root = ListNode(0)
        carry=0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1=l1.next
            if l2:
                carry += l2.val
                l2=l2.next
            root.next = ListNode(carry%10)
            root = root.next
            carry = carry//10
        return output.next