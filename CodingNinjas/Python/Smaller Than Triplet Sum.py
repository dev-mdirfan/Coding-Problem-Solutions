# Problem Link: https://www.codingninjas.com/studio/problems/3-sum-smaller_3161884


# ===================================================================================================
# Time: O(n^3) using brute force
# Space: O(1)
def threeSumSmaller1(n: int, arr: List[int], target: int) -> int:
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] < target:
                    count += 1
    return count


# ===================================================================================================
# Time: O(n^2logn) using binary search
# Space: O(1)
def threeSumSmaller2(n: int, arr: List[int], target: int) -> int:
    arr.sort()
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            count += findPair1(arr, j+1, target-arr[i]-arr[j])
    return count

def findPair1(arr, start, target):
    count = 0
    end = len(arr)-1
    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] < target:
            count += mid - start + 1
            start = mid + 1
        else:
            end = mid - 1
    return count


# ===================================================================================================
# Time: O(n^2) using Two Pointer
# Space: O(1)
def threeSumSmaller(n: int, arr: List[int], target: int) -> int:
    arr.sort()
    count = 0
    for i in range(n):
        count += findPair2(arr, i+1, target-arr[i])
    return count

def findPair2(arr, start, target):
    count = 0
    end = len(arr)-1
    while start < end:
        if arr[start] + arr[end] < target:
            count += end - start
            start += 1
        else:
            end -= 1
    return count
