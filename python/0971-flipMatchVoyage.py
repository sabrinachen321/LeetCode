# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.flipList = []
        self.index = 0
        self.recursive(root, voyage)
        return self.flipList 
    
    def recursive(self, node: TreeNode, voyage: List[int]):
        if not node:
            return
        if node.val != voyage[self.index]:
            self.flipList = [-1]
            return
        self.index += 1
        if node.left and node.right:
            if node.left.val != voyage[self.index]:
                temp = node.left
                node.left = node.right
                node.right = temp
                self.flipList.append(node.val)
        self.recursive(node.left, voyage)
        self.recursive(node.right, voyage)