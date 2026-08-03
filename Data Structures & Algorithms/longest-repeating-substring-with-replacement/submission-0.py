class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxl = 0
        max_freq = 0
        
        for r in range(len(s)):
            char = s[r]
            freq[char] = freq.get(char, 0) + 1
            
            max_freq = max(max_freq, freq[char])
            
            window_len = r - l + 1
            if (window_len - max_freq) > k:
                left_char = s[l]
                freq[left_char] -= 1
                l += 1

            maxl = max(maxl, r - l + 1)
            
        return maxl