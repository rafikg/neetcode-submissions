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

        prod, zeros_cnt = 1, 0
        for num in nums:
            if num:
                prod*=num
            else:
                zeros_cnt+=1
        if zeros_cnt>1:
            return [0]*len(nums)
        output = [0]*len(nums)
        for i, c in enumerate(nums):
            if zeros_cnt:
                output[i] = 0 if c else prod # c!=0
            else:
                # no zero exist
                output[i]=prod//c
        return output
