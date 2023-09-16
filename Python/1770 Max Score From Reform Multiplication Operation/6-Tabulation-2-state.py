#  Tabulation: 2 state: O()
from math import inf
class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        dp=[[ 0 ] * (len(multipliers) + 1) for i in range(len(multipliers) + 1)]
        for operation in range(len(multipliers) - 1, -1, -1):
            for left in range(operation, -1, -1):
                leftAns = nums[left] * multipliers[operation] + dp[operation + 1][left + 1]
                rightAns = nums[(len(nums) - 1) - (operation - left)] * multipliers[operation] + dp[operation + 1][left]
                dp[operation][left] = max(leftAns, rightAns)
        return dp[0][0]