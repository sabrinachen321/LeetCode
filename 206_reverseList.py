# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def recursive(prev, node):
        	if not node:
        		return None
        	nextNode = node.next
        	node.next = prev
        	if not nextNode:
        		return node
        	return recursive(node, nextNode)

        def iterative(head):
        	newHead = ListNode(-1)
        	node = head
        	while node:
        		nextNode = node.next
        		node.next = newHead.next
        		newHead.next = node
        		node = nextNode
        	return newHead.next

        return iterative(head)
