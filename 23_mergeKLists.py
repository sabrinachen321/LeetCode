# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge(l1, l2):
        	newHead = ListNode(0)
        	node = newHead
        	while l1 and l2:
        		if l1.val <= l2.val:
        			node.next = l1
        			l1 = l1.next
        		else:
        			node.next = l2
        			l2 = l2.next
        		node = node.next
        	if l1:
        		node.next = l1
        	else:
        		node.next = l2
        	return newHead.next

        def devide(lists, start, end):
        	if end < start:
        		return None
        	if start == end:
        		return lists[start]
        	half = (start + end) / 2
        	return merge(devide(lists, start, half), devide(lists, half + 1, end))

        return devide(lists, 0, len(lists) - 1)
