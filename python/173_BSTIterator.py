from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.node = root
        self.q = deque([])
        self.findLeftMost()
        

    def findLeftMost(self):
        if self.node or self.q:
            while self.node:
                self.q.append(self.node)
                self.node = self.node.left
            self.node = self.q.pop()


    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        curNode = self.node
        self.node = self.node.right
        self.findLeftMost()
        return curNode.val
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.node is not None
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
