# Problem Link: https://practice.geeksforgeeks.org/problems/binary-array-sorting-1587115620/1


# Brute Force
# Time: O(logn) using sorting
# Space: O(1)
class Solution1:
    def binSort(self, A, N): 
        A.sort()
        return A


# Time: O(n) using counting sort
# Space: O(1)
class Solution2:
    def binSort(self, A, N):
        count_0 = A.count(0)
        count_1 = A.count(1)
        count_2 = A.count(2)
        A[:] = [0] * count_0 + [1] * count_1 + [2] * count_2
        return A


# Time: O(n) using Two Pointers
# Space: O(1)
class Solution:
    def binSort(self, A, N):
        low, high = 0, len(A)-1
        while low <= high:
            if A[low] == 0:
                low += 1
            else:
                A[low], A[high] = A[high], A[low]
                high -= 1
        return A
