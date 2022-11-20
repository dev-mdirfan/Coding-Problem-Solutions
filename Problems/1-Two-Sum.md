# Two Sum

### Approach 1: Hash Map

**Solution 1:**

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            a = target-nums[i]
            if a in d :
                return [d[a], i]
            else:
                d[nums[i]] = i
```

**Solution 2:**

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            if remaining in seen:
                return [i, seen[remaining]]
            seen[value] = i
```

**Solution 3:**

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target-nums[i]) in nums and nums.index(target-nums[i]) != i:
                return (i, nums.index(target-nums[i]))
```

**Solution 4:**

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            p = target-nums[i]
            copy = nums[i+1:]
            if p in copy:
                # return [i, nums.index(p)]
                return [i, copy.index(p)+i+1]
```

**Solution 5:**

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    l = [i,j]
        return l
```

### Approach 2: Brute Force : O(n^2)
```
# Brute Force : O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            current = nums[i]
            for j in range(i+1, n):
                if current + nums[j] == target:
                    return [i, j]
```

```
# Another way is of thinking -
# Brute Force : O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            current = nums[i]
            search = target - current
            for j in range(i+1, n):
                if search == nums[j]:
                    return [i, j]
```
