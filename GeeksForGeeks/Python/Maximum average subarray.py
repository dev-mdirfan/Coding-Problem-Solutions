# Problem Link: https://practice.geeksforgeeks.org/problems/maximum-average-subarray5859/1

# Time: O(n^2) using brute force [TLE]
# Space: O(1)
class Solution1:
    def findMaxAverage(self, arr, n, k):
        answer = []
        for i in range(n-k+1):
            total = 0
            for j in range(i, i+k):
                total += arr[j]
            answer.append(total)
        return answer.index(max(answer))


# Time: O(n) using prefix sum
# Space: O(n)
class Solution2:
    def findMaxAverage(self, arr, n, k):
        answer, prefixSum = [], [0]
        for i in range(n):
            prefixSum.append(prefixSum[-1] + arr[i])
        for i in range(n-k+1):
            answer.append(prefixSum[i+k] - prefixSum[i])
        return answer.index(max(answer))


# Time: O(n) using slidign window
# Space: O(1)
class Solution:
    def findMaxAverage(self, arr, n, k):
        wStart, wSum, answer = 0, 0, []
        for wEnd in range(n):
            wSum += arr[wEnd]
            if wEnd >= k-1:
                answer.append(wSum)
                wSum -= arr[wStart]
                wStart += 1
        return answer.index(max(answer))
