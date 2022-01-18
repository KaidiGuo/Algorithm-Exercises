# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
This is the clear way.
1.Pick the first element of preorder list as root.
2.find the index of this element in inorder list.
3.left tree has new inorder list [0:index];
  right tree has new inorder list [index+1:]
4.left tree has new preorder list [1 : len(new left inorder list)];
  right tree has new preorder list [len(new left inorder list)+1 :]
5. set root.left = self.buildTree(new left preorder, new left inorder)
   set root.right = self.buildTree(new right preorder, new right preorder)
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        new_root_ind = inorder.index(root_val)

        left_inorder = inorder[:new_root_ind]
        right_inorder = inorder[new_root_ind + 1:]
        left_preorder = preorder[1:len(left_inorder) + 1]
        right_preorder = preorder[len(left_inorder) + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root
'''
but actually, when we say root.left = self.buildTree(preorder)
the left subtree of the root will be constructed totally before we go to the right part
so we can optimize a little bit
no need to slice the preorder list into two left-right part,
merely let it pop out the first element in every recursion
so when the code runs to line root.right = self.buildTree(preorder,right_inorder)
what left of preorder list is exactly the same as above right_preorder
but do keep in mind, in this way, we MUST put root.left=self.buildtree() BEFORE root.right=self.buildTree()
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        new_root_ind = inorder.index(root_val)

        left_inorder = inorder[:new_root_ind]
        right_inorder = inorder[new_root_ind + 1:]
        # left_preorder = preorder[1:len(left_inorder)+1]
        # right_preorder = preorder[len(left_inorder)+1:]
        preorder.pop(0)

        root.left = self.buildTree(preorder, left_inorder)
        root.right = self.buildTree(preorder, right_inorder)

        return root