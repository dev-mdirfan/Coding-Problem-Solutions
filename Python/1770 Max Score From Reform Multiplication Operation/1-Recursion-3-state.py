# Recursion TC : O(2^m)
class Solution:
    def helper(self, nums, multipliers, operation, left, right):
        if operation == len(multipliers):
            return 0
        leftAns = nums[left] * multipliers[operation] + self.helper(nums, multipliers, operation + 1, left + 1, right)
        rightAns = nums[right] * multipliers[operation] + self.helper(nums, multipliers, operation + 1, left, right - 1)
        return max(leftAns, rightAns)
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        return self.helper(nums, multipliers, 0, 0, len(nums)-1)

if __name__ == '__main__':
    pass