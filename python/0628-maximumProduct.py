class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def arrangeMost(l, size, num, postivie):
            if len(l) < size:
                l.append(num)
                l.sort(reverse=postivie)
                return
            for i in range(0, len(l)):
                if (postivie and num > l[i]) or (not postivie and num < l[i]):
                    l.insert(i, num)
                    l.pop()
                    return

        neg, pos = [], []
        for num in nums:
            if num <= 0:
                arrangeMost(neg, 3, num, False)
            elif num > 0:
                arrangeMost(pos, 3, num, True)
        most = neg + pos
        maxProduct = most[0] * most[1] * most[2]
        for i in range(0, len(most) - 2):
            for j in range(i + 1, len(most) - 1):
                for k in range(j + 1, len(most)):
                    maxProduct = max(maxProduct, most[i] * most[j] * most[k])
        return maxProduct