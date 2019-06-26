from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.q = deque([root])
        while self.q[0].left and self.q[0].right:
            node = self.q.popleft()
            self.q.append(node.left)
            self.q.append(node.right)
        if self.q[0].left:
            self.q.append(self.q[0].left)


    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = TreeNode(v)
        parent = self.q[0]
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
            self.q.popleft()
        self.q.append(node)
        return parent.val
        

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
