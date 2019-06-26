# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head is not None and head.val == val:
        	head = head.next
        ret = previous = head
        while head is not None:
        	head = head.next
        	if head is not None and head.val == val:
        		previous.next = head.next
        	else:
        		previous = head
        return ret
