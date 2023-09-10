# Memo TC : O(2^m) 2 states
from math import inf
class Solution:
    def helper(self, nums, multipliers, operation, left, dp):
        if operation == len(multipliers):
            return 0
        if dp[operation][left] != -1:
            return dp[operation][left]
        leftAns = nums[left] * multipliers[operation] + self.helper(nums, multipliers, operation + 1, left + 1, dp)
        rightAns = nums[(len(nums) - 1) - (operation - left)] * multipliers[operation] + self.helper(nums, multipliers, operation + 1, left, dp)
        dp[operation][left] = max(leftAns, rightAns)
        return dp[operation][left]
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        # dp=[[ -inf ] * len(multipliers) for i in range(len(nums))]
        dp=[[ -1 ] * len(multipliers) for i in range(len(nums))]
        # print(dp)
        return self.helper(nums, multipliers, 0, 0, dp)