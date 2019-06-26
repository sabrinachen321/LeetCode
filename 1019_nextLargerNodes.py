from collections import deque

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        ret = []
        q = deque([])
        nodeIndex = {}
        index = 0
        while head:
        	while q and q[len(q) - 1].val < head.val:
        		node = q.pop()
        		ret[nodeIndex[node]] = head.val
        	q.append(head)
        	ret.append(0)
        	nodeIndex[head] = index
        	head = head.next
        	index += 1
        return ret
