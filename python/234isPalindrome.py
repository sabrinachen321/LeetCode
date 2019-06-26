# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def iterative(head):
        	newHead = ListNode(-1)
        	node = head
        	while node:
        		nextNode = node.next
        		node.next = newHead.next
        		newHead.next = node
        		node = nextNode
        	return newHead.next

        fast = slow = head
        while fast and fast.next:
        	fast = fast.next.next
        	slow = slow.next
        secondHalf = iterative(slow)
        node1, node2 = head, secondHalf
        while node1 and node2:
        	if node1.val != node2.val:
        		return False
        	node1, node2 = node1.next, node2.next
        iterative(secondHalf)
        return True