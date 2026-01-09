class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for s in strs:
            sSorted = "".join(sorted(s))
            if sSorted in dict1:
                dict1[sSorted].append(s)
            else:
                dict1[sSorted] = [s]
        return list(dict1.values())
                
        

        