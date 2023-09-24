# Problem Link: https://leetcode.com/problems/sort-colors/


# Time: O(nlogn) using sorting [Not In-place]
# Space: O(1)
class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return nums.sort()


# Time: O(n) using count sort [Not In-place]
# Space: O(1)
class Solution2:
    def sortColors1(self, nums: List[int]) -> None:
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for i in nums:
            if i == 0:
                count_0 += 1
            elif i == 1:
                count_1 += 1
            else:
                count_2 += 1
        for i in range(count_0):
            nums[i] = 0
        for i in range(count_0, count_0 + count_1):
            nums[i] = 1
        for i in range(count_0 + count_1, count_0 + count_1 + count_2):
            nums[i] = 2
        return nums

    def sortColors2(self, nums: List[int]) -> None:
        count_0 = nums.count(0)
        count_1 = nums.count(1)
        count_2 = nums.count(2)
        # nums[:] = [0] * count_0 + [1] * count_1 + [2] * count_2
        nums[:count_0] = [0] * count_0
        nums[count_0 : count_0 + count_1] = [1] * count_1
        nums[count_0 + count_1 :] = [2] * count_2
        return nums


# Time: O(n) using 3 pointers
# Space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
        return nums
