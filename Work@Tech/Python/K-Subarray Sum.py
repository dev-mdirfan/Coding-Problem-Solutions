# Time Complexity: O(n3) using brute force [TLE]
# Space Complexity: O(1)
class Solution1:
    def kSubarraySum(self, A: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(A)):
            for j in range(i, len(A)):
                if sum(A[i:j+1]) == k:
                    ans.append(A[i:j+1])
        return ans


# Time: O(n^2) using slicing [TLE]
# Space: O(1)
class Solution2:
    def kSubarraySum(self, A: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(A)-k+1):
            window = A[i : i+k]
            ans.append(sum(window))
        return ans
    
    # without using sum() or slicing
    def kSubarraySum1(self, A: List[int], k: int) -> List[int]:
        ans = []
        n = len(A)
        for i in range(n-k+1):
            total = 0
            for j in range(i, i+k):
                total += A[j]
            ans.append(total)
        return ans


# Time: O(n) using prefix sum
# Space: O(n)
class Solution3:
    def kSubarraySum(self, A: List[int], k: int) -> List[int]:
        prefixSum, ans = [0], []
        for i in range(len(A)):
            prefixSum.append(prefixSum[-1] + A[i])
        for i in range(len(A)-k+1):
            s = prefixSum[i+k] - prefixSum[i]
            ans.append(s)
        return ans


# Time: O(n) using sliding window
# Space: O(1)
class Solution4:
    def kSubarraySum1(self, A: List[int], k: int) -> List[int]:
        wSum, ws, we, ans = 0, 0, 0, []
        while we < len(A):
            if we - ws + 1 <= k:
                wSum += A[we]
            else:
                ans.append(wSum)
                wSum -= A[ws]
                wSum += A[we]
                ws += 1
            we += 1
        ans.append(wSum)
        return ans
    
    def kSubarraySum2(self, A: List[int], k: int) -> List[int]:
        wSum, ws, we, ans = 0, 0, 0, []
        while we < len(A):
            wSum += A[we]
            if we-ws+1 < k:
                we += 1
            elif we-ws+1 == k:
                ans.append(wSum)
                wSum -= A[ws]
                ws += 1
                we += 1
        return ans
    
    def kSubarraySum3(self, A: List[int], k: int) -> List[int]:
        i, n = 0, len(A)
        ans = []
        s = sum(A[ : k])
        ans.append(s)
        while i < n-k:
            s = s - A[i] + A[i + k]
            ans.append(s)
            i += 1
        return ans
    
    def kSubarraySum3(self, A: List[int], k: int) -> List[int]:
        ws = 0
        wSum = 0
        ans = []
        for we in range(len(A)):
            wSum += A[we]
            # if we >= k-1:
            if we-ws+1 == k:
                ans.append(wSum)
                wSum -= A[ws]
                ws += 1
        return ans
