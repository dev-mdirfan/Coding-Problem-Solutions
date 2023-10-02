# Problem Link: https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

# Time: O(n^2) uisng brute force [TLE]
# Space: O(1)
class Solution1:
    def maximumSumSubarray (self,K,Arr,N):
        maxSum = -float('inf')
        for i in range(N-K+1):
            s = 0
            for j in range(i, i+K):
                s += Arr[j]
            maxSum = max(maxSum, s)
        return maxSum



# Time: O(n) using prefix sum
# Space: O(n)
class Solution2:
    def maximumSumSubarray (self,K,Arr,N):
        prefixSum, maxSum = [0], -float('inf')
        for i in range(N):
            prefixSum.append(prefixSum[-1] + Arr[i])
        for i in range(N-K+1):
            s = prefixSum[i+K] - prefixSum[i]
            maxSum = max(maxSum, s)
        return maxSum


# Time: O(n) using sliding window
# Space: O(1)
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        wStart, wSum, answer = 0, 0, []
        for wEnd in range(N):
            wSum += Arr[wEnd]
            if wEnd >= K-1:
                answer.append(wSum)
                wSum -= Arr[wStart]
                wStart += 1
        return max(answer)
