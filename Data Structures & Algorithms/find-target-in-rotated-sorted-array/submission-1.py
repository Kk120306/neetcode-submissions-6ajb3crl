class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if the number we are at at the middle is bigger than target, we check if the very left of that number is still bigger 
        # If not we look to the right of the array, if not we look left of the array, keep track of the index we are at 

        l, r = 0, len(nums) - 1

        while l <= r: 
            mid = (l + r) // 2
            midNum = nums[mid]
            if midNum == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # right half sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
