class Solution:
    def canJump(self, nums: List[int]) -> bool:
            n = len(nums)
            t = [False]*n

            t[0]=True

            for i in range(1, n):
                for j in range(i-1, -1, -1):
                    if t[j]==True and j+nums[j]>=i:
                        t[i]=True
                        break

            return t[n-1]

