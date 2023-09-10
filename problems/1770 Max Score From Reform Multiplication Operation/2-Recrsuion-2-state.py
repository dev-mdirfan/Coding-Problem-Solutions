# Recursion TC : O(2^m) 2 states
class Solution:
    def helper(self, nums, multipliers, operation, left):
        if operation == len(multipliers):
            return 0
        leftAns = nums[left] * multipliers[operation] + self.helper(nums, multipliers, operation + 1, left + 1)
        rightAns = nums[(len(nums) - 1) - (operation - left)] * multipliers[operation] + self.helper(nums, multipliers, operation + 1, left,)
        return max(leftAns, rightAns)
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        return self.helper(nums, multipliers, 0, 0)