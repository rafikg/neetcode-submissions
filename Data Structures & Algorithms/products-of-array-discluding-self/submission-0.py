import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prod = math.prod(nums)
        for  i in range(len(nums)):
            v = nums[i]
            if v==0:
                r = int(math.prod(nums[:i])*math.prod(nums[i+1:]))
            else:
                r= int(prod/v)
            output.append(r)
        return output
        