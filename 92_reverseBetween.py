# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
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

        newHead = ListNode(-1)
        newNode = newHead
        part1s = part1e = part2s = part2e = part3s = None
        pos = 1
        node = head
        while node:
        	if pos == 1:
        		part1s = node
        	if pos == m - 1:
        		part1e = node
        	if pos == m:
        		part2s = node
        	if pos == n:
        		part2e = node
        	if pos == n + 1:
        		part3s = node
        	if pos > n + 1:
        		break
        	node = node.next
        	pos += 1
        part2e.next = None
        part2e = part2s
        part2s = iterative(part2s)
        part2e.next = part3s
        if m > 1:
        	newNode.next = part1s
        	newNode = part1e
        newNode.next = part2s
        return newHead.next
