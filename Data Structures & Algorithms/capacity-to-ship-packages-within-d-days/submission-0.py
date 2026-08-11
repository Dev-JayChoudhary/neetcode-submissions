class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l,r=max(weights), sum(weights)
        res=r

        def canship(cap):
            ships, currcap=1 ,cap
            for w in weights:
                if currcap- w<0:
                    ships+=1
                    currcap=cap
                currcap-=w
            return ships<=days

        while l<=r:
            mid=(l+r)//2
            if canship(mid):
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res

