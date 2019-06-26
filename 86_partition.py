# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        firstHead = ListNode(-1)
        secondHead = ListNode(-1)
        first = firstHead
        second = secondHead
        node = head
        while node:
        	if node.val < x:
        		first.next = node
        		first = first.next
        	else:
        		second.next = node
        		second = second.next
        	node = node.next
        first.next = secondHead.next
        second.next = None
        return firstHead.next
