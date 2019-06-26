# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        length = 0
        node = head
        while node:
        	length += 1
        	node = node.next
        if length < 3:
            return head

        second = head
        for i in range(int(length / 2) + 1):
        	prev = second
        	second = second.next
        prev.next = None

        prev = None
        node = second
        while node:
        	nextNode = node.next
        	node.next = prev
        	prev = node
        	node = nextNode

        tail = prev
        newHead = ListNode(-1)
        newNode = newHead
        while tail:
        	nextHead = head.next
        	nextTail = tail.next
        	newNode.next = head
        	newNode.next.next = tail
        	newNode = newNode.next.next
        	head = nextHead
        	tail = nextTail
        newNode.next = head
        return newHead.next
