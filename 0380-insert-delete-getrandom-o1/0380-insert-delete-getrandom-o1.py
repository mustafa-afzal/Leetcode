import random

class RandomizedSet:

    def __init__(self):
        self.randomizedSet = set()
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.randomizedSet:
            return False
        self.randomizedSet.add(val)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.randomizedSet:
            self.randomizedSet.remove(val)
            self.list.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        length = len(self.randomizedSet)
        randIdx = random.randint(0, length - 1)
        return self.list[randIdx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()