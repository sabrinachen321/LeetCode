# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        node = root
        length = 0
        while node:
        	length += 1
        	node = node.next

        size, mod = length / k, length % k
        ret = []
        node = root
        for i in range(k):
        	ret.append(node)
        	realSize = size
        	if i < mod:
        		realSize += 1
        	for j in range(realSize - 1):
        		node = node.next
        	if node:
        		nextNode = node.next
        		node.next, node = None, nextNode
        return ret
