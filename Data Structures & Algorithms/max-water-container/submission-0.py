class Solution:
    # def maxArea(self, heights: List[int]) -> int:
    #     max_area=0
    #     for i in range(len(heights)):
    #         for j in range(i+1,  len(heights)):
    #             height = min(heights[i],heights[j])
    #             width = abs(i-j)
    #             area = width*height
    #             if area>max_area:
    #                 max_area=area
    #     return max_area
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max_area = 0
        while(left<right):
            height = min(heights[left],heights[right])
            width = abs(right-left)
            if max_area < height*width:
                max_area = height*width
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
        return max_area







        