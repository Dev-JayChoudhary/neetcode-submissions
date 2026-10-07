class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        maxe=nums[0]

        for i in range(1,len(nums)):
            maxe=max(maxe+nums[i], nums[i])
            res= max(maxe, res)

        return res
