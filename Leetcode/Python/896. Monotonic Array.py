# Problem Link: https://leetcode.com/problems/monotonic-array/


# Time: O(nlogn) using sorting
# Space: O(1)
class Solution1:
    def isMonotonic(self, nums: List[int]) -> bool:
        return sorted(nums) == nums or sorted(nums, reverse=True) == nums


# Time: O(n) using first element greater then it should be greater
# Space: O(1)
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        flag = False
        index = 1
        while index < n:
            if nums[index] == nums[index-1]:
                index += 1
            else:
                if nums[index] > nums[index-1]:
                    flag = True
                break
        if flag:
            while index < n:
                if nums[index] < nums[index-1]:
                    return False
                index += 1
        else:
            while index < n:
                if nums[index] > nums[index-1]:
                    return False
                index += 1
        return True

# One Liner
class Solution:
    def isMonotonic(self, A):
        # return not {cmp(i, j) for i, j in zip(A, A[1:])} >= {1, -1}   ## cmp == (i>j)-(i<j)
        # return not { (i>j)-(i<j) for i, j in zip(A, A[1:])} >= {1, -1}
        # return len({x < y for x, y in zip(A, A[1:]) if x != y}) <= 1
        return all(A[i] <= A[i+1] for i in range(len(A) - 1)) or all(A[i] >= A[i+1] for i in range(len(A) - 1))
