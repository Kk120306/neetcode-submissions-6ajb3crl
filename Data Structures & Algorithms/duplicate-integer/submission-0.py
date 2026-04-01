class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copy = set(nums)
        return len(copy) != len(nums)