# Problem Link: https://practice.geeksforgeeks.org/problems/triplets-with-sum-with-given-range/1

# Time: O(n^3) using brute force [TLE]
# Space: O(1)
class Solution1:
    def countTriplets(self, arr, n, L, R):
        count = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if L <= arr[i] + arr[j] + arr[k] <= R:
                        count += 1
        return count


# Time: O(n^2logn) using binary search [TLE]
# Space: O(1)
class Solution2:
    def countTriplets(self, arr, n, L, R):
        arr.sort()
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                count += self.findPair(arr, arr[i], arr[j], j+1, R) - self.findPair(arr, arr[i], arr[j], j+1, L)
        return count
    
    def findPair(self, arr, first, sec, start, target):
        end = len(arr) - 1
        count = 0
        while start <= end:
            mid = start + (end - start) // 2
            if first + sec + arr[mid] <= target:
                count += mid - start + 1
                start = mid + 1
            else:
                end = mid - 1
        return count


# Time: O(n^2) using dictionary
# Space: O(n) for dictionary
# ===========================================================================


# Time: O(n^2) using two pointer
# Space: O(1)
class Solution:
    def countTriplets(self, arr, n, L, R):
        arr.sort()
        count = 0
        for i in range(n):
            count += self.findPair(arr, i+1, R, arr[i]) - self.findPair(arr, i+1, L-1, arr[i])
        return count
    
    def findPair(self, arr, start, target, first):
        end = len(arr) - 1
        count = 0
        while start < end:
            if first + arr[start] + arr[end] <= target:
                count += end - start
                start += 1
            else:
                end -= 1
        return count
