class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphaNum(c):
            return (ord("A")<=ord(c)<=ord("Z") or
                ord("a")<=ord(c)<=ord("z") or    
                ord("0")<=ord(c)<=ord("9")
            )
            
        front = 0
        back = len(s) - 1
        
        while front < back:
            while front < back and not alphaNum(s[front]):
                front += 1
            while back > front and not alphaNum(s[back]):
                back -= 1
                
            if s[front].lower() != s[back].lower():
                return False
                
            front += 1
            back -= 1
            
        return True