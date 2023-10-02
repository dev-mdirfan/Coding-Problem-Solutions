# Problem Link: https://leetcode.com/problems/backspace-string-compare/


# Time: O(n) uisng 
# Space: O(n)
class Solution1:
    def validString(self, s):
        right = len(s) - 1
        check = ''
        hashCount = 0
        while right >= 0:
            if s[right] != '#' and hashCount > 0:
                hashCount -= 1
            elif s[right] != '#' and hashCount == 0:
                check = s[right] + check
            else:
                while right >= 0 and s[right] == '#':
                    hashCount += 1
                    right -= 1
                right += 1
            right -= 1
        return check
    def backspaceCompare(self, s: str, t: str) -> bool:
        valid_1 = self.validString(s)
        valid_2 = self.validString(t)
        if valid_1 == valid_2:
            return True
        else:
            False


# Time: O(n) using Two Pointer
# Space: O(1)
class Solution:
    def validIndex(self, string, index):
        backspace = 0
        while index >= 0:
            if string[index] == '#':
                backspace += 1
            elif backspace > 0:
                backspace -= 1
            else:
                break
            index -= 1
        return index
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s)-1, len(t)-1
        while i >= 0 or j >= 0:
            VI1 = self.validIndex(s, i)
            VI2 = self.validIndex(t, j)
            if VI1 < 0 and VI2 < 0:
                return True
            elif VI1 < 0 or VI2 < 0:
                return False
            elif s[VI1] != t[VI2]:
                return False
            i = VI1 - 1
            j = VI2 - 1
        return True
