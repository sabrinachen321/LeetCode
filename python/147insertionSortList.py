# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(0)
        node = head
        while node:
        	newNode = newHead
        	while newNode.next and newNode.next.val <= node.val:
        		newNode = newNode.next
        	oldNoxt = node.next
        	newNext = newNode.next
        	newNode.next = node
        	node.next = newNext
        	node = oldNoxt
        return newHead.next
