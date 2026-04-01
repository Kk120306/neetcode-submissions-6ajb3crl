class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            val = abs(nums[i])
            target = nums[val]

            if target < 0:
                return val
            
            nums[val] *= -1


