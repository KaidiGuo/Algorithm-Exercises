# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
BFS exercise here.
Similar to question 107. Traverse the tree layer by layer. Store each layer in a list.
See if all the list are symmetrical.
Note: During the traverse, we need to put an "null" value at the position of each missing child,
otherwise situation like [null,3,null,3] will be omitted into [3,3], thus judged wrongly as symmetrical.
"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        queue = []
        results = []
        if root: queue.append(root)
        while queue:
            layer = []
            next_queue = []
            while queue:
                first_node = queue[0]
                queue.pop(0)
                if first_node == "NULL":
                    layer.append("NULL")
                else:
                    layer.append(first_node.val)
                    if first_node.left:
                        next_queue.append(first_node.left)
                    else:
                        next_queue.append("NULL")
                    if first_node.right:
                        next_queue.append(first_node.right)
                    else:
                        next_queue.append("NULL")
            results.append(layer)
            queue = next_queue

        for li in results:
            re = list(reversed(li))
            if re != li:
                return False
        return True