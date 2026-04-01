class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0
        res = 0

        for right in range(len(s)): 
            c = s[right]

            if c in last and last[c] >= left:
                left = last[c] + 1
            
            last[c] = right
            res = max(res, right-left + 1)

        return res

