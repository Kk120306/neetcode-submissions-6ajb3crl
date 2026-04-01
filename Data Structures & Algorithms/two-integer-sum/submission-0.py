class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        result = []

        for index, num in enumerate(nums):
            remaining = target - num
            if remaining in table: 
                result.append(table[remaining])
                result.append(index)
                break
            else:
                table[num] = index
                
        return result

