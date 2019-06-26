class MapSum(object): 

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(0)


    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        # self.root.count = self.root.count + val
        node = self.root
        for k in key:
            node = node.addChild(k, val)
        if node.isEnd:
            node = self.root
            for k in key:
                node = node.getChild(k)
                node.count = node.count - node.lastCount
                node.lastCount = val
        else:
            node.isEnd = True
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for p in prefix:
            node = node.getChild(p)
            if node is None:
                return 0
        return node.count
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

class Node(object):
    
    def __init__(self, count):
        self.children = { }
        self.count = count
        self.isEnd = False
        self.lastCount = count

    def addChild(self, letter, val):
        if self.children.has_key(letter):
            self.children[letter].count = self.children[letter].count + val
        else:
            self.children[letter] = Node(val)
        return self.children[letter]

    def getChild(self, letter):
        if self.children.has_key(letter):
            return self.children[letter]
        else:
            return None
