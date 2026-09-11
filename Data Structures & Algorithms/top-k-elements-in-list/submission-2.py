from collections import defaultdict
from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         d = defaultdict(int)
#         for x in nums:
#             d[x]+=1
#         # sorted d
#         sorted_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
#         keys = list(sorted_d.keys())
#         return keys[:k]
        
# Time Complexity
# O(n*nlog(k)) where n is the length of the table
# Space complexity
# O(n+m)=O(n) where m is the unique number of values in nums

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = dict(Counter (nums))
        tab = [[] for _ in range(len(nums))]
        
        for k_, v_ in c.items():
            tab[v_-1].append(k_)
        # tab = [x for x in tab if x]
        res = []
        for i in  range(len(tab)-1, -1, -1):
            x = tab[i]
            if not x:
                continue
            res.extend(x[:k-len(res)])
            if len(res) == k:
                return res
        
            



         
        