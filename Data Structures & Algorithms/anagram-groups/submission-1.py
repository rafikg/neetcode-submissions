# Sorting approach
# from collections import defaultdict
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         d= defaultdict(list[str])
#         for x in strs:
#             sorted_x = "".join(sorted(x))
#             d[sorted_x].append(x)

#         # return only values of d as list of list
#         return list(d.values())           

# Time Complexity:
# O(m*nlogn) where m is the number of strings
# Space Complexity:
# O(m*n) where n is the longest string

# Hash Table approach
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for s in strs:
            count_idx = [0]*26
            for c  in s:
                count_idx[ord(c) - ord('a')]+=1
            d[tuple(count_idx)].append(s)
        return list(d.values())  