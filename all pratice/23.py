#1046,leetcode,easy
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        elif len(stones)==0:
            return 0
        stones.sort()
        last1,last2=stones.pop(),stones.pop()
        if last1!=last2:
            stones.append(last1-last2)
        return self.lastStoneWeight(stones)
#递归写法

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones):
            stones.sort()
            last1,last2=stones.pop(),stones.pop()
            if last1!=last2:
                stones.append(last1-last2)
            else:
                continue
        if len(stones)==1:
            return stones[0]
        elif len(stones)==0:
            return 0
#while写法


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        list1=[-i for i in stones]
        heapq.heapify(list1)
        while len(list1)>1:
            a=-heapq.heappop(list1)
            b=-heapq.heappop(list1)
            if a!=b:
                heapq.heappush(list1,-a+b)
        return -list1[0] if list1 else 0
#堆写法－－获得最大／最小值的算法