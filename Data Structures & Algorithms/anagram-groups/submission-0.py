class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}

        for i in range(len(strs)):
            x = "".join(sorted(strs[i]))
            if x in mydict:
                mydict[x].append(strs[i])
            
            else:
                mydict[x] = [(strs[i])]
            
        return list(mydict.values())
            








