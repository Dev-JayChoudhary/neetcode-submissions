class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap={}
        arr=[]
        for i in range(len(nums)):
            myMap[nums[i]]=1+myMap.get(nums[i], 0)
        sorted_nums = sorted(myMap.keys(), key=lambda x: myMap[x], reverse=True)
        return sorted_nums[:k]