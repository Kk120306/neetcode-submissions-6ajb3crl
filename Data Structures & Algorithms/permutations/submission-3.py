class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res = []

        # def dfs(cur, remaining):
        #     if not remaining:
        #         res.append(cur.copy())
        #         return
            
        #     for i in range(len(remaining)):
        #         cur.append(remaining[i])
        #         dfs(cur, remaining[:i] + remaining[i+1:])
        #         cur.pop()
            
        # dfs([], nums)
        # return res

        if len(nums) == 0:
            return [[]]
        
        perm = self.permute(nums[1:])
        res = []
        for p in perm:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        
        return res
