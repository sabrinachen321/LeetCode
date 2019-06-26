# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(-1)
        newNode = newHead
        prev = None
        node = head
        while node:
        	if (not prev or prev.val != node.val) and (not node.next or node.val != node.next.val):
        		newNode.next = node
        		newNode = newNode.next
        	prev = node
        	node = node.next
        newNode.next = None
        return newHead.next
