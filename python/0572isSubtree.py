from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSame(s, t):
        	if not s and not t:
        		return True
        	elif s and t:
        		return s.val == t.val and isSame(s.left, t.left) and isSame(s.right, t.right)
        	else:
        		return False

        def recursive(s, t):
        	if not s:
        		return False
        	else:
        		return isSame(s, t) or recursive(s.left, t) or recursive(s.right, t)

        return recursive(s, t)
