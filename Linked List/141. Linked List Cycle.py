# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited={}
        while head:
            if head in visited.keys():
                print("visited")
                return True
            else:
                visited[head]=1
                head = head.next
                
        return False