# Problem Link: https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

# Time: O(nlogn) using sorting
# Space: O(1)
class Solution1:
    def sort012(self,arr,n):
        arr.sort()
        return arr


# Time: O(n) using counting sort
# Space: O(1)
class Solution2:
    def sort012(self,arr,n):
        count_0, count_1, count_2 = arr.count(0), arr.count(1), arr.count(2)
        arr[ : count_0] = [0] * count_0
        arr[count_0 : count_1] = [1] * count_1
        arr[count_0 + count_1 : ] = [2] * count_2
        return arr


# Time: O(n) using 3 pointers
# Space: O(1)
class Solution:
    def sort012(self,arr,n):
        left, mid, right = 0, 0, len(arr)-1
        while mid <= right:
            if arr[mid] == 0:
                arr[left], arr[mid] = arr[mid], arr[left]
                left += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[right], arr[mid] = arr[mid], arr[right]
                right -= 1

