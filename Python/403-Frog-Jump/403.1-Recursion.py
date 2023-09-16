# Recursion: T(n) = ?
# Pure Recursion: TLE
class Solution:
    def solve(self, currentPosition, previousJump):
        # Second Invalid Condition
        if previousJump <= 0:
            return False
        # Third Invalid Condition
        if currentPosition not in self.stones:
            return False
        # Valid Condition Only in reaching end of the stones
        if currentPosition == self.stones[-1]:
            return True
        # Recursion
        return self.solve(currentPosition + previousJump - 1, previousJump - 1) or self.solve(currentPosition + previousJump, previousJump) or self.solve(currentPosition + previousJump + 1, previousJump + 1)
    
    def canCross(self, stones: list[int]) -> bool:
        self.stones = stones
        # First Invalid Condition
        if stones[1] != 1:
            return False
        return self.solve(1, 1)

if __name__ == '__main__':
    stones1 = [0, 1, 3, 5, 6, 8, 12, 17]
    stones2 = [0 ,1 ,2 ,3 ,4 ,8 ,9 ,11]
    obj = Solution()
    print(stones1,':',obj.canCross(stones1))
    print(stones2,':',obj.canCross(stones2))