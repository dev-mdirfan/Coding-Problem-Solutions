#  Tabulation
from math import inf
class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        m = len(multipliers)
        dp = [ 0 ] * (m + 1)
        for operation in range(m):
            mult = multipliers[m - 1 - operation]
            # at round m, we  pick the m-th multiplier
            # at round m - 1, we pick the (m - 1) - ith multiplier
            # at round m - 2, we pick the (m - 2) - ith multiplier
            # and so on ... 
            for left in range(m - operation):
                # how many elements we need to process? 
                # at round m, there are m elements
                # at round m - 1, there are m - 1 elements
                # at round m - 2, there are m - 2 elements
                # and so on ...
                leftAns = nums[left] * mult + dp[left + 1]
                rightAns = nums[left + len(nums) - (m - operation)] * mult + dp[left]
                dp[left] = max(leftAns, rightAns)
        return dp[0]