class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0
        l,r = 0, len(heights)-1
        while l<r:
            water = (r-l)*(min(heights[l], heights[r]))
            max_water=max(max_water, water)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_water