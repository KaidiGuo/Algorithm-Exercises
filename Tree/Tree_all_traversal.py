
#           [1]
#           / \
#         [2]  [3]
#         / \   
#       [4]  [5]
# 
#
# Depth First Traversals: 
# (a) Inorder (Left, Root, Right) : 4 2 5 1 3 
# (b) Preorder (Root, Left, Right) : 1 2 4 5 3 
# (c) Postorder (Left, Right, Root) : 4 5 2 3 1
# Breadth-First or Level Order Traversal: 1 2 3 4 5 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# We prefer iterative than recursion because recursion algorithms have an overhead for procedure calls




# compare two tree is identical
def identical(s, t):
    if s is None and t is None:
        return True
    if s is not None and t is not None:
        return s.val == t.val and identical(s.left, t.left) and identical(s.right, t.right)
    return False

# using stack
def preorder_stack(self ,s: TreeNode):
    res =""
    stack = []
    while s or stack:
        while s:
            res = res + str(s.val)
            stack.append(s)
            s = s.left
        s = stack.pop()
        s = s.right
    return res


def inorder_stack(s):
    res = ""
    stack = []
    while s or stack:
        while s:
            stack.append(s)
            s = s.left
        s = stack.pop()
        res += str(s.val)
        s = s.right
    return res

# Note that, the postorder is the reversed [right-root-left] traversal, and preorder is [left-root-right] traversal
# so we can reuse the preorder code, merely change the s=s.left to s=s.right, and in the end, return revered traversal results
def postorder_stack(s):
    res = ""
    stack = []
    while s or stack:
        while s:
            res += str(s.val)
            stack.append(s)
            s = s.right
        s = stack.pop()
        s = s.left
    res = res[::-1]
    return res

