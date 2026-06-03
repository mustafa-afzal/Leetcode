class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sSorted = ""
        map = {}
        for s in strs:
            sSorted = "".join(sorted(s))
            if sSorted in map:
                map[sSorted].append(s)
            else:
                map[sSorted] = [s]
        return list(map.values())