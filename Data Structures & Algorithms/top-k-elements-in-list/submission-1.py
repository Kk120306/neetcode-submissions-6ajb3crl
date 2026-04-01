class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        frequencyTable = {}
        for num in nums:
            if num in frequencyTable:
                frequencyTable[num] += 1
            else:
                frequencyTable[num] = 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in frequencyTable.items():
            bucket[freq].append(num)
        
        for i in range(len(bucket) -1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

        