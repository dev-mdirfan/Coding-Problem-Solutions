# Problem Link: https://practice.geeksforgeeks.org/problems/count-triplets-with-sum-smaller-than-x5549/1


# ===================================================================================================
# Time: O(n^3) using brute force [TLE]
# Space: O(1)
class Solution1:
    def countTriplets(self, arr, n, sumo):
        count = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if arr[i] + arr[j] + arr[k] < sumo:
                        count += 1
        return count


# ===================================================================================================
# Time: O(n^2 log n) using binary search
# Space: O(1)
class Solution2:
    def countTriplets(self, arr, n, sumo):
        arr.sort()
        count = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                target = sumo - arr[i] - arr[j]
                count += self.binarySearch(arr, j+1, n-1, target)
        return count
    
    def binarySearch(self, arr, start, end, target):
        count = 0
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] < target:
                count += mid - start + 1
                start = mid + 1
            else:
                end = mid - 1
        return count


# ===================================================================================================
# Time: O(n^2) using two pointer
# Space: O(1)
class Solution:
    def countTriplets(self, arr, n, sumo):
        arr.sort()
        count = 0
        for i in range(n):
            count += self.findPair(arr, i+1, sumo - arr[i])
        return count
    
    def findPair(self, arr, start, target):
        end = len(arr) - 1
        count = 0
        while start < end:
            if arr[start] + arr[end] < target:
                count += end - start
                start += 1
            else:
                end -= 1
        return count
