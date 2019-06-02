#Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p and not q) or (not p and q):
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)


root2 = TreeNode(5)
root2.left = TreeNode(4)
root2.right = TreeNode(9)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(1)

root3 = None

sol1 = Solution()
print(sol1.isSameTree(root, root3))