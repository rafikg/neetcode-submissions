from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d= defaultdict(list[str])
        for x in strs:
            sorted_x = "".join(sorted(x))
            d[sorted_x].append(x)

        # return only values of d as list of list
        return list(d.values())                
                
        