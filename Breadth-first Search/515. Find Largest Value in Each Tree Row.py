# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Practice float('-inf')
"""
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return None
        maxs=[]
        queue=[root]
        while queue:
            next_queue=[]
            m = float('-inf')
            for node in queue:
                m = max(node.val,m)
                if node.left: next_queue.append(node.left)
                if node.right: next_queue.append(node.right)
            queue=next_queue
            maxs.append(m)
        return maxs