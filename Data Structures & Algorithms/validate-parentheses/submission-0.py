class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brac_map = {")":"(","]":"[", "}":"{"}

        for c in s:
            if c in brac_map:
                if stack and stack[-1]== brac_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            
            


