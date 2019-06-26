# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddHead = odd = ListNode(-1)
        evenHead = even = ListNode(-1)
        while head:
        	odd.next = head
        	odd = odd.next
        	even.next = head.next
        	even = even.next
        	if head.next:
        		head = head.next.next
        	else:
        		break
        odd.next = evenHead.next
        return oddHead.next
