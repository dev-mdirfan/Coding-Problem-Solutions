# 403. Frog Jump
# BFS without queue: O( ? )
class Solution:
    def canCross(self, stones: list[int]) -> bool:
        graph = dict()
        
        # creating dict of set
        for stone in stones:
            graph[stone] = set()
        
        graph[0].add(1)
        
        for currPosition in stones:
            jumps = graph[currPosition]
            for jump in jumps:
                newPosition = currPosition + jump
                # If reach end return True
                if newPosition == stones[-1]:
                    return True
                # if stone position exits then add next jumps
                if newPosition in graph:
                    if jump - 1 > 0:
                        graph[newPosition].add(jump - 1)
                    graph[newPosition].add(jump)
                    graph[newPosition].add(jump + 1)
        return False

if __name__ == '__main__':
    stones1 = [0, 1, 3, 5, 6, 8, 12, 17]
    stones2 = [0 ,1 ,2 ,3 ,4 ,8 ,9 ,11]
    obj = Solution()
    print(stones1,':',obj.canCross(stones1))
    print(stones2,':',obj.canCross(stones2))