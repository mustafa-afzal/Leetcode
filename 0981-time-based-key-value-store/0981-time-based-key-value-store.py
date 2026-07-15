class TimeMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.hmap.get(key):
            self.hmap[key].append((timestamp, value))
        else:
            self.hmap[key] = [(timestamp, value)]
 
    def get(self, key: str, timestamp: int) -> str:
        pairs = self.hmap.get(key)
        if not pairs:
            return ""
        else: 
            length = len(pairs) - 1
        l, r = 0, length
        bestVal = ""
        while l <= r:
            m = (l + r) // 2
            if pairs[m][0] > timestamp:
                r = m - 1
            else:
                bestVal = pairs[m][1]
                l = m + 1
        return bestVal

      

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)