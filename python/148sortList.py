# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge(l1, l2):
        	newHead = ListNode(0)
        	node = newHead
        	while l1 and l2:
        		if l1.val <= l2. val:
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

        def devide(head):
        	if not head or not head.next:
        		return head
        	slow = fast = head
        	while fast and fast.next:
        		prev = slow
        		slow = slow.next
        		fast = fast.next.next
        	prev.next = None
        	return merge(devide(head), devide(slow))

        return devide(head)
