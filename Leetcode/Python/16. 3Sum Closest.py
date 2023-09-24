# Problem Link: https://leetcode.com/problems/3sum-closest/

# Time: O(n ^3) using brute force
# Space: O(1)
class Solution1:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    s = nums[i] + nums[j] + nums[k]
                    if s == target:
                        return s
                    elif abs(s - target) < abs(result - target):
                        result = s
        return result


# Time: O(n^2 logn) using binary search
# Space: O(1)
class Solution2:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        self.result = nums[0] + nums[1] + nums[2]
        for i in range(n):
            for j in range(i+1, n):
                self.findThird(nums, j+1, target, nums[i], nums[j])
        return self.result

    def findThird(self, arr, start, target, first, sec):
        end = len(arr) - 1
        while start <= end:
            mid = start + (end - start)//2
            totalSum = first + sec + arr[mid]
            if totalSum == target:
                self.result = totalSum
                return
            elif abs(totalSum - target) < abs(self.result - target):
                self.result = totalSum
            elif totalSum < target:
                start = mid + 1
            elif totalSum > target:
                end = mid - 1


# Time: O(n^2) using Two Pointers
# Ṣpace: O(1)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        self.result = nums[0] + nums[1] + nums[2]
        for i in range(n):
            self.findPair(nums, i+1, target, nums[i])
        return self.result
    
    def findPair(self, arr, start, target, first):
        end = len(arr)-1
        while start < end:
            totalSum = first + arr[start] + arr[end]
            if totalSum == target:
                self.result = totalSum
                return
            elif abs(totalSum - target) < abs(self.result - target):
                self.result = totalSum
            elif totalSum < target:
                start += 1
            elif totalSum > target:
                end -= 1
