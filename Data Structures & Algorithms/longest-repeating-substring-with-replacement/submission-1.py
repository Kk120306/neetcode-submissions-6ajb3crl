class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Start with left as 0 
        # Iterate num right by 1 each time 
        # check if that window size - most freq char in the hash table 
        # is less than or equal to k value. Once equal update the max v
        # Once more or equal then we index the left val by 1 and repeat calc
        res = 0
        left = 0 
        maxFreq = 0
        freq = {}
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxFreq = max(freq[s[right]], maxFreq)

            if right - left + 1 - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res




