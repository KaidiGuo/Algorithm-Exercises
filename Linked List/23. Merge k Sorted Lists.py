# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h=[]
        result = ListNode()
        curr= result
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(h, (head.val,i, head))

        while h:
            _,i,node = heapq.heappop(h)
            curr.next=node
            if node.next:
                heapq.heappush(h,(node.next.val,i,node.next))
            curr = curr.next
        return result.next
