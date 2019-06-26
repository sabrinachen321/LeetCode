# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def inorder(node, s, e):
        	if s > e:
        		return [node, None]
        	h = (s + e) / 2
        	[curNode, left] = inorder(node, s, h - 1)
        	treeNode = TreeNode(curNode.val)
        	treeNode.left = left
        	[nextNode, treeNode.right] = inorder(curNode.next, h + 1, e)
        	return [nextNode, treeNode]

        length = 0
        itr = head
        while itr:
        	length += 1
        	itr = itr.next

        return inorder(head, 0, length - 1)[1]
