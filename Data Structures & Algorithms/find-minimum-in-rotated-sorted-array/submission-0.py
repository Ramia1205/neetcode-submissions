class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid is greater than the rightmost value,
            # the minimum must be to the RIGHT of mid.
            if nums[mid] > nums[right]:
                left = mid + 1

            # Otherwise, the minimum is at mid
            # or somewhere to the LEFT of mid.
            else:
                right = mid

        return nums[left]