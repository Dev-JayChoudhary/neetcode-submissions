class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) ==0:
            return 0
        if len(s)==1:
            return 1


        freq = {}
        l,r = 0 ,0
        maxl=0
        while r<len(s):
            char = s[r]
            if freq.get(char, 0)>0:
                freq[s[l]]-=1
                l=l+1
            else :
                freq[char]=1
                maxl = max(maxl, r-l+1)
                r=r+1
                
        
        return maxl

            