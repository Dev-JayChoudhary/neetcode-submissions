class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReachable=0

        for i in range(len(nums)):
            if i>maxReachable:
                return False
            maxReachable = max(maxReachable, nums[i]+i)
            if maxReachable==len(nums)-1:
                return True
            

        return True
