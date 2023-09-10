# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted


# Time: O(n^2) using Brute Force
# Space: O(1)
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            first_number = numbers[i]
            for j in range(i+1, n):
                second_number = numbers[j]
                if first_number + second_number == target:
                    return [i + 1, j + 1]


# Time: O(n) using dictionary
# Space: O(n)
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = dict()
        for i in range(len(numbers)):
            new_target = target - numbers[i]
            if new_target not in hash_map:
                hash_map[numbers[i]] = i + 1
            else:
                return [hash_map[new_target], i + 1] 


# Time: O(n * log n) using Binary Search
# Space: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        # O(n)
        for i in range(n):
            left, right = i + 1, n - 1    # search subarray
            new_target = target - numbers[i]
            # O(log n)
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == new_target:
                    return [i+1, mid+1]
                elif numbers[mid] < new_target:
                    left = mid + 1
                else:
                    right = mid - 1


# Time: O(n) using Two Pointer
# Space: O(1)
class Solution3:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
    
    # reduce lines
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1]
