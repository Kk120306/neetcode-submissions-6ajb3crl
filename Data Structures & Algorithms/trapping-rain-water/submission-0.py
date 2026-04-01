class Solution:
    def trap(self, height: List[int]) -> int:
        # Iterate from left to right 
        # If we find area add to ttl area
        # Iterate the min side 
        # If there is hight > current on the +1 or -1 side, remove previous area 
        # iterate until there height of next <=current 
        # add col 

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res