from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def recursive(p, q):
        	if not p and not q:
        		return True
        	elif p and q and p.val == q.val:
        		return recursive(p.left, q.left) and recursive(p.right, q.right)
        	else:
        		return False

        def iterative(root1, root2):
        	q = deque([root1, root2])
        	while len(q) >= 2:
        		a = q.pop()
        		b = q.pop()
        		if (a and not b) or (not a and b) or (a and b and a.val != b.val):
        			return False
        		if a and b:
        			q.extend([a.left, b.left, a.right, b.right])
        	return True

        return iterative(p, q)
