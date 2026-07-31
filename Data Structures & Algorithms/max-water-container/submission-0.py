class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        a = 0
        while i < j:
            area = min(heights[i], heights[j]) * (j-i)
            if area > a:
                a = area
            if min(heights[i], heights[j]) == heights[i]:
                i += 1
            else:
                j -= 1
        return a














        9