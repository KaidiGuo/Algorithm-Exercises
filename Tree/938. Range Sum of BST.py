# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = []
        s=0
        while root or stack:
            while root:
                stack.append(root)
                if root.val > low:
                    root=root.left
                else:
                    break
            root = stack.pop()
            if low <= root.val <= high:
                s+=root.val
            if root.val < high:
                root = root.right
            else:
                root=None
        return s

# Since the tree is already sorted, 
# we add two if statements to stop the search of sub left/right tree when root.val is out of the boundary