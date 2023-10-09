# Problem Link: https://leetcode.com/problems/subarray-sum-equals-k/


# Time: O(n^3) using Brute Force
# Space: O(1)
class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, n = 0, len(nums)
        for i in range(n):
            for j in range(i, n):
                if sum(nums[i : j+1]) == k:
                    count += 1
        return count


# Time: O(n^2) using prefix sum
# Space: O(n)
class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n, prefixSum, count = len(nums), [0], 0
        for i in range(n):
            prefixSum.append(prefixSum[-1] + nums[i])
        for i in range(n+1):
            for j in range(i+1, n+1):
                if prefixSum[j] - prefixSum[i] == k:
                    count += 1
        return count


# Time: O(n^2) using Brute Force
# Space: O(1)
class Solution3:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n, count = len(nums), 0
        for i in range(n):
            subArraySum = 0
            for j in range(i, n):
                subArraySum += nums[j]
                if subArraySum == k:
                    count += 1
        return count


# Time: O(n) using prefix sum frequency and sliding window
# Space: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = {0: 1}  # A dictionary to store the prefix sum frequencies
        current_sum = 0
        for num in nums:
            current_sum += num
            # Check if (current_sum - k) exists in prefix_sum, indicating a subarray sum of k
            if current_sum - k in prefix_sum:
                count += prefix_sum[current_sum - k]
            # Update the prefix_sum dictionary
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        return count
