class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        for num in nums1:
        	if dic.has_key(num):
        		dic[num] += 1
        	else:
        		dic[num] = 1
        ret = []
        for num in nums2:
        	if dic.has_key(num) and dic[num] > 0:
        		dic[num] -= 1
        		ret.append(num)
        return ret
