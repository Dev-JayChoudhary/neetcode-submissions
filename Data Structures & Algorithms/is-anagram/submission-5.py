class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list_t = list(t)

        for i in s:
            if i in list_t:
                list_t.remove(i)
            else:
                return False

        return True