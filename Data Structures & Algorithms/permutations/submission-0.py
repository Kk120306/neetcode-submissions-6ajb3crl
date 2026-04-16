class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        
        def dfs(cur, remaining):
            if not remaining:
                res.append(cur.copy())
                return
            
            for i in range(len(remaining)):
                cur.append(remaining[i])
                dfs(cur, remaining[:i] + remaining[i+1:])
                cur.pop()
            
        dfs([], nums)
        return res
