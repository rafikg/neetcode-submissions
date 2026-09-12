import math
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         output = []
#         prod = math.prod(nums)
#         for  i in range(len(nums)):
#             v = nums[i]
#             if v==0:
#                 r = int(math.prod(nums[:i])*math.prod(nums[i+1:]))
#             else:
#                 r= int(prod/v)
#             output.append(r)
#         return output

# Time complexity:
# O(n^2)
# Space complexity
# O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = math.prod([x for x in nums if x!=0])
        number_zeros = len([x for x in nums if x==0])
        if number_zeros >=2:
            return [0]*len(nums)
        output = []
        if number_zeros ==1:    
            for  i in range(len(nums)):
                v = nums[i]
                if v==0:
                    r = int(prod)
                else:
                    r= 0
                output.append(r)
            return output
        for i in range(len(nums)):
            
            v = nums[i]
            r= prod//v
            output.append(r)
        return output

        