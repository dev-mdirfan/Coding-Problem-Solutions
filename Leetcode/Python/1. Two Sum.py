# Problem Link: https://leetcode.com/problems/two-sum/


# Time: O(n^2) using brute force
# Space: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            current = nums[i]
            for j in range(i+1, n):
                if current + nums[j] == target:
                    return [i, j]
        return []
    
    # using enumerate
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums[index1 + 1:]):
                if num1 + num2 == target:
                    return [index1, index2 + index1 + 1]
        return []
    
    # or using in operator
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            p = target-nums[i]
            copy = nums[i+1:]
            if p in copy:
                # return [i, nums.index(p)]
                return [i, copy.index(p)+i+1]
    
    # or using index
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target-nums[i]) in nums and nums.index(target-nums[i]) != i:
                return (i, nums.index(target-nums[i]))


# Time: O(n) using hash table
# Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            if remaining in seen:
                return [i, seen[remaining]]
            seen[value] = i
        return []


# Time: O(nlogn) using two pointers
# Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(num, index) for index, num in enumerate(nums)]
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left][0] + nums[right][0] == target:
                return [nums[left][1], nums[right][1]]
            elif nums[left][0] + nums[right][0] > target:
                right -= 1
            else:
                left += 1
        return []
