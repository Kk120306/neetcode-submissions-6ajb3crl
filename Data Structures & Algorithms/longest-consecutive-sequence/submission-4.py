class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        maxStreak = 0

        for num in uniqueNums:
            if num-1 not in uniqueNums:
                current = num
                length = 1

                while current + 1 in uniqueNums:
                    current += 1
                    length += 1
                
                maxStreak = max(maxStreak, length)
         
        
        return maxStreak
