class TimeMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.hmap.get(key):
            self.hmap[key].append((timestamp, value))
        else:
            self.hmap[key] = []
            self.hmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.hmap.get(key)
        bestVal = -1
        if pairs:
            length = len(pairs)
        else:
            length = 0
        l, r = 0, length - 1
        while l <= r:
            m = (l + r) // 2
            if pairs[m][0] > timestamp:
                r = m - 1
            elif pairs[m][0] <= timestamp:
                bestVal = pairs[m][1]
                l = m + 1
        return bestVal if bestVal != -1 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)