# https://leetcode.com/problems/squares-of-a-sorted-array/


# Time: O(n log n) using sorting
class Solution1:
    # Space: O(n)
    def sortedSquares1(self, nums: List[int]) -> List[int]:
        new_nums = list()
        for element in nums:
            new_nums.append(element ** 2)
        return sorted(new_nums)

    # Space: O(1)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        return sorted(nums)


# Time: O(n) using Two Pointers
# Space: O(n)
class Solution:
    # using insert
    def sortedSquares1(self, nums: List[int]) -> List[int]:
        ans = []
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                ans.insert(0, nums[left] ** 2)
                left += 1
            else:
                ans.insert(0, nums[right] ** 2)
                right -= 1
        return ans

    # using append
    def sortedSquares2(self, nums: List[int]) -> List[int]:
        array = list()
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                array.append(nums[left] ** 2)
                left += 1
            else:
                array.append(nums[right] ** 2)
                right -= 1
        return array[: : -1]

    # using index
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        array = [0] * n
        left, right, index = 0, n-1, n-1
        while left <= right:
            lsquare = nums[left] ** 2 
            rsquare = nums[right] ** 2
            if lsquare > rsquare:
                array[index] = lsquare
                left += 1
            else:
                array[index] = rsquare
                right -= 1
            index -= 1
        return array




