class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f= 0
        l = len(numbers)-1
        while f<l:
            if (numbers[f]+numbers[l])>target:
                l-=1
            elif (numbers[f]+numbers[l])<target:
                f+=1
            elif (numbers[f]+numbers[l])==target:
                return [f+1,l+1]
        return []
                
        
