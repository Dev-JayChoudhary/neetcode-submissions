class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset=set()
        for i in range(len(nums)):
            if not (nums[i] in myset):
                myset.add(nums[i])
            else:
                return True
        
        return False