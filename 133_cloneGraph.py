from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
        	return None
        newNode = Node(node.val, [])
        nodeMap = { node : newNode }
        q = deque([node, newNode])
        while q:
        	itr = q.popleft()
        	newItr = q.popleft()
        	for neighbor in itr.neighbors:
        		newNeighbor = nodeMap.get(neighbor, Node(neighbor.val, []))
        		newItr.neighbors.append(newNeighbor)
        		if (not nodeMap.has_key(neighbor)):
        			q.append(neighbor)
        			q.append(newNeighbor)
        			nodeMap[neighbor] = newNeighbor
        return newNode
        
