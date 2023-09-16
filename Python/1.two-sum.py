# https://leetcode-cn.com/problems/two-sum/

# Using hash table
# Time: O(n)
# Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for index, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], index]
            hash_table[num] = index
        return []


# Using two pointers
# Time: O(nlogn)
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


# Using brute force
# Time: O(n^2)
# Space: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums[index1 + 1:]):
                if num1 + num2 == target:
                    return [index1, index2 + index1 + 1]
        return []





