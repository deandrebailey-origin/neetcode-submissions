class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = -1
        l, r = 0, len(heights) - 1

        while l <= r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height

            best = max(best, area)
            if heights[l] > heights[r]:
                r -= 1
            else: 
                l += 1
        return best