# Problem Link: https://leetcode.com/problems/sort-array-by-parity/


# Time: O(n) using two loops
# Space: O(n)
class Solution1:
    def sortArrayByParity1(self, nums: List[int]) -> List[int]:
        answer = []
        for even in nums:
            if even % 2 == 0:
                answer.append(even)
        for odd in nums:
            if odd % 2 != 0:
                answer.append(odd)
        return answer

    def sortArrayByParity2(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        index, left, right = 0, 0, len(nums)-1
        # while index < len(nums):
        while left <= right:
            if nums[index] % 2 == 0:
                answer[left] = nums[index]
                left += 1
            else:
                answer[right] = nums[index]
                right -= 1
            index += 1
        return answer


# Time: O(n) using Two Pointer & Swap
# Space: O(1)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] % 2 != 0:
                nums[right], nums[left] = nums[left], nums[right]
                right -= 1
            else:
                left += 1
        return nums
