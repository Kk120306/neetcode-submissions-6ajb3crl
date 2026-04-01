class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Start from left 0 and right max 
        # get the maxium 
        # calc distance away and get math min of the two index 
        # well see fi the right - 1 or left + 1 is bigger than prev 
        # if not bigger check for both left and right 

        l = 0 
        r = len(heights) - 1 
        res = 0

        while l < r: 
            leftHeight = heights[l]
            rightHeight = heights[r]
            area = (r - l) * min(leftHeight, rightHeight)
            res = max(res, area)

            if leftHeight >= rightHeight: 
                while l < r:
                    r -= 1
                    if rightHeight < heights[r]:
                        break
            else:
                while l < r:
                    l += 1
                    if leftHeight < heights[l]:
                        break

    
        return res
