"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
        	return None
        node = head
        newHead = Node(head.val, head.next, None)
        newNode = newHead
        while node.next is not None:
        	newNode.next = Node(node.next.val, None, None)
        	node = node.next
        	newNode = newNode.next
        node = head
        newNode = newHead
        while node is not None and newNode is not None:
        	nextNode = node.next
        	nextNewNode = newNode.next
        	newNode.next = node.next
        	node.next = newNode
        	node = nextNode
        	newNode = nextNewNode
        node = head
        while node is not None and node.next is not None:
        	if node.random is not None:
        		node.next.random = node.random.next
        	else:
        		node.next.random = None
        	node = node.next.next
        node = head
        while node is not None:
        	nextNode = node.next
        	if nextNode is not None:
        		node.next = nextNode.next
        	else:
        		node.next = None
        	node = nextNode
        return newHead
