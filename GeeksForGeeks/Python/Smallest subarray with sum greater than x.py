# Problem Link: https://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1

# Time: O(n^3) using brute force [TLE]
# Space: O(1)
class Solution1:
    def smallestSubWithSum(self, a, n, x):
        minLength = n
        for i in range(n):
            for j in range(i, n):
                if sum(a[i : j+1]) > x:
                    minLength = min(minLength, j+1 - i)
                    break
        return minLength


# Time: O(n^2) using prefix sum [TLE]
# Space: O(n)
class Solution2:
    def smallestSubWithSum1(self, a, n, x):
        prefixSum = [0]
        minLength = n
        for i in range(n):
            prefixSum.append(prefixSum[-1] + a[i])
        for i in range(n+1):
            for j in range(i+1, n+1):
                if prefixSum[j] - prefixSum[i] > x:
                    minLength = min(minLength, j-i)
                    break
        return minLength


# Time: O(n^2) using loops [TLE]
# Space: O(1)
class Solution3:
    def smallestSubWithSum(self, a, n, x):
        minLength = 10**4+1
        for i in range(n):
            sum_all = 0
            for j in range(i, n):
                sum_all += a[j]
                if sum_all > x:
                    minLength = min(minLength, j-i+1)
        return minLength


# Time: O(n) using sliding window & Prefix sum
# Space: O(n)
class Solution4:
    def smallestSubWithSum(self, a, n, x):
        wStart, wEnd, minLength, prefixSum = 0, 0, n, [0]
        for i in range(n):
            prefixSum.append(prefixSum[-1] + a[i])
        flag = 1    # for not having > x ans should be 0
        while wEnd <= n:
            if prefixSum[wEnd] - prefixSum[wStart] > x:
                minLength = min(minLength, wEnd - wStart)
                wStart += 1
                flag = 0
            else:
                wEnd += 1
        if flag:
            return 0
        return minLength


# Time: O(n) using sliding window
# Space: O(1)
class Solution:
    def smallestSubWithSum1(self, a, n, x):
        wStart, wEnd, wSum, minLength, = 0, 0, 0, n
        flag = 1
        while wSum > x or wEnd < n:
            if wSum > x:
                # print(wEnd-wStart)
                minLength = min(minLength, wEnd-wStart)
                wSum -= a[wStart]
                wStart += 1
                flag = 0
            else:
                wSum += a[wEnd]
                wEnd += 1
        if flag:
            return 0
        return minLength
    
    def smallestSubWithSum(self, a, n, x):
        start, end, minLength, windowSum = 0, 0, n+1, 0
        flag = 1
        while start <= end and  end<n:
            while windowSum <= x and end<n:
                windowSum += a[end]
                end += 1
            while windowSum > x and start < end:
                flag = 0
                minLength = min(minLength, end-start)
                windowSum -= a[start]
                start += 1
        if flag:
            return 0
        return minLength