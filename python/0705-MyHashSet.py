# 用list实现的，其实还可以用树结构实现，理论上的时间复杂度会是log而不是线性

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.hashList = [[] for i in range(self.size)]
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashList[key % self.size].append(key)
        

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashList[key % self.size].remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        for _, item in enumerate(self.hashList[key % self.size]):
            if item == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)