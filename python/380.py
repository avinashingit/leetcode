class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = {}
        self.elements = []
        self.l = 0


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.index:
            return False
        self.index[val] = self.l
        self.elements.append(val)
        self.l += 1
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        index = self.index.get(val, -1)
        if index == -1:
            return False
        self.index[self.elements[-1]] = index
        self.elements[index] = self.elements[-1]
        self.elements.pop()
        self.l -= 1
        del self.index[val]
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        return random.choice(self.elements)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
