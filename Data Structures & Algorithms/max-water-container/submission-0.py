class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            # Width between the two lines
            width = right - left

            # Water height is limited by the shorter line
            height = min(heights[left], heights[right])

            # Current container area
            area = width * height

            # Keep the best area seen so far
            max_area = max(max_area, area)

            # Move the shorter side inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area