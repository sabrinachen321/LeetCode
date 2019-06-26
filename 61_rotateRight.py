# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
        	return head
        node = head
        length = 0
        while node:
        	length += 1
        	node = node.next
        k = k % length
        fast = slow = head
        for i in range(k):
        	fast = fast.next
        while fast.next:
        	fast = fast.next
        	slow = slow.next
        fast.next = head
        newHead = slow.next
        slow.next = None
        return newHead
