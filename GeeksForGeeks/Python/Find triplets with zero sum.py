# Time: O(n^3) brute force [TLE]
# Space: O(1)
class Solution1: 
    def findTriplets(self, arr, n):
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if arr[i] + arr[j] + arr[k] == 0:
                        return 1
        return 0


# Time: O(n^2logn) using binary search [TLE]
# Space: O(1)
class Solution2: 
    def findTriplets(self, arr, n):
        arr.sort()
        for i in range(n):
            target = -arr[i]
            if self.findPair(arr, i+1, target):
                return 1
        return 0
    
    def findPair(self, arr, i, target):
        for j in range(i, len(arr)):
            if self.binarySearch(arr, j+1, target - arr[j]):
                return True
    
    def binarySearch(self, arr, left, target):
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left)//2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


# Time: O(n^2) using dictionary
# Space: O(n) for dictionary
class Solution3: 
    def findTriplets(self, arr, n):
        for i in range(n):
            if self.findPair(arr, i+1, -arr[i]):
                return 1
        return 0
    
    def findPair(self, arr, start, target):
        end = len(arr)
        hash_map = dict()
        for j in range(start, n):
            if target - arr[j] in hash_map:
                return True
            hash_map[arr[j]] = j
        return False


# Time: O(n^2) using two pointer
# Space: O(1)
class Solution: 
    def findTriplets(self, arr, n):
        arr.sort()
        for i in range(n):
            if self.findPair(arr, i+1, -arr[i]):
                return 1
        return 0
    
    def findPair(self, arr, start, target):
        end = len(arr) - 1
        while start < end:
            if arr[start] + arr[end] == target:
                return True
            elif arr[start] + arr[end] < target:
                start += 1
            else:
                end -= 1
        return False
