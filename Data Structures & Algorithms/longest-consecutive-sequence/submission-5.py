# from collections import Counter
# class UnionFind:
#     def __init__(self, n):
#         self.parent = list(range(n))
#     def find(self, i):
#         if self.parent[i]!=i:
#             self.parent[i]= self.find(self.parent[i])
#         return self.parent[i]
        
#     def union(self, i, j):
#         rep_i = self.find(i)
#         rep_j = self.find(j)
#         self.parent[rep_i]=rep_j

    

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if len(nums)==0:
#             return 0
#         d = {}
#         uds = UnionFind(len(nums))
#         for i, v in enumerate(nums):
#             if v not in d:
#                 d[v]=i
        
#         for x in d:
#             if x-1 in d:
#                 uds.union(d[x], d[x-1])

#         # search for the different groups
#         res=[]
#         for k,v in d.items():
#             res.append(uds.find(v))
#         most_common_item, max_count = Counter(res).most_common(1)[0]
#         return max_count

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest=0
        for num in nums:
            if num-1 not in set_nums:
                length=1
                while (num+length) in set_nums:
                    length+=1
                longest = max(longest, length)
        return longest

        