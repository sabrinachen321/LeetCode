class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.hashList = [[] for i in range(self.size)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket = key % self.size
        if self.get(key) == -1:
            self.hashList[bucket].append((key, value))
        else:
            index = -1
            for i, (k, v) in enumerate(self.hashList[bucket]):
                if k == key:
                    index = i
                    break
            self.hashList[bucket][index] = (key, value)

        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for _, (k, v) in enumerate(self.hashList[key % self.size]):
            if key == k:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        value = self.get(key)
        if value != -1:
            self.hashList[key % self.size].remove((key, value))
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)