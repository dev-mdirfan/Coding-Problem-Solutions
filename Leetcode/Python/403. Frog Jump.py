# Problem Link: https://leetcode.com/problems/frog-jump/

# Time: O(n^2) using dictionary (TLE)
# Space: O(n^2)
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones:
            return False
        if stones[1] != 1:
            return False
        n = len(stones)
        dp = [[False for _ in range(n)] for _ in range(n)]
        dp[0][0] = True
        for i in range(1, n):
            for j in range(i):
                diff = stones[i] - stones[j]
                if diff < 0 or diff >= n or not dp[j][diff]:
                    continue
                dp[i][diff] = True
                if diff - 1 >= 0:
                    dp[i][diff-1] = True
                if diff + 1 < n:
                    dp[i][diff+1] = True
        return any(dp[-1])

