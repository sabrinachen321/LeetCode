# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def findSubNodeK(node, subNodeList, K):
        	if not node:
        		return
        	if K == 0:
        		subNodeList.append(node.val)
        	else:
        		findSubNodeK(node.left, subNodeList, K - 1)
        		findSubNodeK(node.right, subNodeList, K - 1)

        def findTarget(node, target, parentList):
        	if not node:
        		return -1
        	if node == target:
        		return 0
        	leftDistance = findTarget(node.left, target, parentList)
        	rightDistance = findTarget(node.right, target, parentList)
        	if leftDistance == -1 and rightDistance == -1:
        		return -1
        	parentList.add(node)
        	return max(leftDistance, rightDistance) + 1

        def dfs(node, parentList, subNodeList, distance, K):
        	if not node:
        		return
        	if distance == 0:
        		findSubNodeK(node, subNodeList, K)
        	elif K <= distance:
        		if K == distance:
        			subNodeList.append(node.val)
        		if node.left in parentList:
        			dfs(node.left, parentList, subNodeList, distance - 1, K)
        		else:
        			dfs(node.right, parentList, subNodeList, distance - 1, K)
        	else:
        		if node.left in parentList:
        			findSubNodeK(node.right, subNodeList, K - distance - 1)
        			dfs(node.left, parentList, subNodeList, distance - 1, K)
        		else:
        			findSubNodeK(node.left, subNodeList, K - distance - 1)
        			dfs(node.right, parentList, subNodeList, distance - 1, K)

        parentList = set([target])
        distance = findTarget(root, target, parentList)
        # print distance
        # for node in parentList:
        # 	print node.val
        nodeList = []
        dfs(root, parentList, nodeList, distance, K)
        return nodeList
