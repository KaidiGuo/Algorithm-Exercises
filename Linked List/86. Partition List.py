# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1, split the notes by value into two lists, use append to keep order of the nodes, 
# re-connect the nodes in the two lists in the end
# This solution is not inplace
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small=[]
        big=[]
        result = ListNode()
        marker=result
        while head:
            if head.val<x:
                small.append(head)
                print(f"small {head.val}")
            else:
                big.append(head)
                print(f"big {head.val}")
            head = head.next

        for item in small:
            item.next=None
            marker.next=item
            marker = marker.next
        for item in big:
            item.next=None
            marker.next=item
            marker = marker.next
        return result.next

#Solution 2
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode()
        big= ListNode()
        ps = small
        pb = big
        while head:
            print(f"head value {head.val}")
            if head.val <x:
                ps.next = head
                ps = head
            else:
                pb.next= head
                pb = head
            head = head.next
        pb.next=None
        
        ps.next = big.next
        return small.next