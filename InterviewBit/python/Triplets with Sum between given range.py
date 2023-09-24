# Problem Link: https://www.interviewbit.com/problems/triplets-with-sum-between-given-range/


# Time: O(n^3) using brute force (TLE)
# Space: O(1)
class Solution1:
	# @param A : list of strings
	# @return an integer
	def solve(self, A):
		n = len(A)
		arr = [float(x) for x in A]
		for i in range(n):
			for j in range(i+1, n):
				for k in range(j+1, n):
					if 1 < arr[i] + arr[j] + arr[k] < 2:
						return 1
		return 0

# Time: O(n^2logn) using binary search (TLE)
# Space: O(1)
class Solution2:
	def solve(self, A):
		arr = sorted([float(x) for x in A])
		n = len(arr)
		for i in range(n):
			for j in range(i+1, n):
				if self.findPair(arr, j+1, arr[i], arr[j]):
					return 1
		return 0
	
	def findPair(self, arr, start, first, sec):
		end = len(arr) - 1
		while start <= end:
			mid = start + (end - start)//2
			if 1 < first + sec + arr[mid]:
				if first + sec + arr[mid] < 2:
					return True
				else:
					end = mid - 1
			else:
				start = mid + 1
		return False

# Time: O(n^2) using Hash Table
# Space: O(1)


# Time: O(n^2) using Two Pointer
# Space: O(1)
class Solution3:
	def solve(self, A):
		arr = sorted([float(x) for x in A])
		n = len(arr)
		for i in range(n):
			if self.findPair(arr, i+1, arr[i]):
				return 1
		return 0
	
	def findPair(self, arr, start, first):
		end = len(arr) - 1
		while start < end:
			if 1 < first + arr[start] + arr[end]:
				if first + arr[start] + arr[end] < 2:
					return True
				else:
					end -= 1
			else:
				start += 1
		return False

# Time: O(nlogn) using Two Pointer
# Space: O(1)
class Solution4:
	def solve1(self, A):
		n = len(A)
		if n < 3:
			return 0
		A.sort()
		start = 0
		end = n - 1
		while end - start >= 2:
			mid = (start + end) // 2
			a = float(A[start])
			b = float(A[mid])
			c = float(A[end])
			wholeSum = a + b + c
			if wholeSum > 1 and wholeSum < 2:
				return 1
			elif wholeSum > 2:
				end -= 1
			else:
				start += 1
		return 0
	
	def solve(self, A):
		n = len(A)
		A.sort()
		left = 0
		right = n - 1

		while left < right - 1:
			_sum = float(A[left]) + float(A[left + 1]) + float(A[right])
			if _sum < 1:
				left += 1
			elif _sum > 2:
				right -= 1
			else:
				return 1
		
		return 0


# Time: O(n) using prefix suffix array
# Space: o(4n) = O(n)
class Solution5:
	def solve(self, A):
		if len(A) < 3:
			return 0
		B = []
		for s in A:
			try:
				B.append(float(s))
			except ValueError:
				return 0
		lmx = [0] * len(A)
		lmn = [0] * len(A)
		rmx = [0] * len(A)
		rmn = [0] * len(A)
		lmx[0] = B[0]
		lmn[0] = B[0]
		rmx[len(B)-1] = B[len(B)-1]
		rmn[len(B)-1] = B[len(B)-1]
		for i in range(1, len(B) - 1):
			lmx[i] = max(lmx[i-1], B[i-1])
			lmn[i] = min(lmn[i-1], B[i-1])
			rmx[len(B)-1-i] = max(rmx[len(B)-i], B[len(B)-i])
			rmn[len(B)-1-i] = min(rmn[len(B)-i], B[len(B)-i])
		for i in range(1, len(B) - 1):
			if B[i] + lmx[i] + rmx[i] > 1.0 and B[i] + lmx[i] + rmx[i] < 2.0:
				return 1
			if B[i] + lmn[i] + rmn[i] > 1.0 and B[i] + lmn[i] + rmn[i] < 2.0:
				return 1
			if B[i] + lmx[i] + rmn[i] > 1.0 and B[i] + lmx[i] + rmn[i] < 2.0:
				return 1
			if B[i] + lmn[i] + rmx[i] > 1.0 and B[i] + lmn[i] + rmx[i] < 2.0:
				return 1
		return 0


# Time: O(n)
# Space: O(1)
class Solution6:
    def solve(self, A):
        n = len(A)
        B = [float(i) for i in A]
        buckets = [[], [], []]
        for i in B:
            if i < 2.0/3:
                buckets[0].append(i)
            elif i < 1:
                buckets[1].append(i)
            else:
                buckets[2].append(i)
        
        def get(index):
            amx1, amx2, amx3 = -10, -10, -10
            ami1, ami2, ami3 = 3, 3, 3
            for i in buckets[index]:
                if i > amx1:
                    amx1, amx2, amx3 = i, amx1, amx2
                elif i > amx2:
                    amx2, amx3 = i, amx2
                elif i > amx3:
                    amx3 = i
            
                if i < ami1:
                    ami1, ami2, ami3 = i, ami1, ami2
                elif i < ami2:
                    ami2, ami3 = i, ami2
                elif i < ami3:
                    ami3 = i
            return [amx1, amx2, amx3, ami1, ami2, ami3]
        
        a = get(0)
        b = get(1)
        c = get(2)
        ls = []
        fc = a[0] + a[1] + a[2]
        ls.append(fc)
        fc = a[3] + a[4] + c[3]
        ls.append(fc)
        fc = a[3] + b[3] + b[4]
        ls.append(fc)
        fc = a[3] + b[3] + c[3]
        ls.append(fc)
        fc = b[0] + a[3] + a[4]
        ls.append(fc)
        if a[0] != a[3]:
            fc = b[0] + a[0] + a[3]
            ls.append(fc)
            fc = b[3] + a[0] + a[3]
            ls.append(fc)
        fc = b[3] + a[0] + a[1]
        ls.append(fc)
        for fc in ls:
            if fc > 1 and fc < 2:
                return 1
        return 0


# Time: O(n)
# Space: o(1)
class Solution7:
	def solve(self, A):
		v = [float(x) for x in A]
		v.sort()
		total_sum = v[0] + v[1] + v[2]
		
		if total_sum >= 2:
			return 0
		elif 1 < total_sum < 2:
			return 1
		else:
			sum1 = total_sum
			for i in range(3, len(v)):
				sum1 -= v[i - 3]
				sum1 += v[i]
				if 1 < sum1 < 2:
					return 1
			
			sum2 = total_sum
			for i in range(3, len(v)):
				sum2 -= v[i - 2]
				sum2 += v[i]
				if 1 < sum2 < 2:
					return 1
			
			sum3 = total_sum
			for i in range(3, len(v)):
				sum3 -= v[i - 1]
				sum3 += v[i]
				if 1 < sum3 < 2:
					return 1
		return 0