# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        prevItr = itr = head
        for i in range(n):
            itr = itr.next
        if not itr:
            return head.next
        while itr.next:
            itr = itr.next
            prevItr = prevItr.next
        prevItr.next = prevItr.next.next
        return head
