# https://leetcode.com/problems/3sum/ 

# Time: O(n^3) using brute force [TLE]
# Space: O(1)
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(arr)
        ans = set()
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if arr[i] + arr[j] + arr[k] == 0:
                        ans.add((arr[i], arr[j], arr[k]))
        return ans


# Time: O(n^2logn) using binary search [TLE]
# Space: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.triplets = set()
        arr = sorted(nums)
        for i in range(len(arr)):
            target = -arr[i]
            self.findPair(arr, i+1, target)
        return self.triplets
    
    def findPair(self, arr, start, target):
        end = len(arr)
        for i in range(start, end):
            new_target = target - arr[i]
            if self.binarySearch(arr, i+1, end-1, new_target):
                self.triplets.add((-target, new_target, arr[i]))
    
    def binarySearch(self, arr, start, end, target):
        while start <= end:
            mid = start + (end-start)//2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False


# Time: O(n^2) using dictionary
# Space: O(n) for dictionary
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.triplets = set()
        arr = sorted(nums)
        for i in range(len(arr)):
            target = -arr[i]
            self.findPair(arr, i+1, target)
        return self.triplets
    
    def findPair(self, arr, start, target):
        end = len(arr)
        hash_map = dict()
        for i in range(start, end):
            new_target = target - arr[i]
            if new_target not in hash_map:
                hash_map[arr[i]] = i
            else:
                self.triplets.add((-target, new_target, arr[i]))


# Time: O(n^2) using two pointer
# Space: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            target = -nums[i]    # To find pair sum to target value arr[i] + arr[j] + arr[k] = 0
            if i > 0 and nums[i] == nums[i-1]:	# To remove duplicate triplets
                continue
            self.find_pair(nums, i+1, target, triplets)
        return triplets
    
    # Time: O(n)
    def find_pair(self, arr, left, target, triplets):
        right = len(arr)-1
        while left < right:
            arrsum = arr[left] + arr[right]
            if arrsum == target:
                triplets.append([-target, arr[left], arr[right]])
                left += 1
                right -= 1
                # To remove duplicate pair
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left<right and arr[right] == arr[right+1]:
                    right -= 1
            elif arrsum < target:
                left += 1
            else:
                right -= 1
