#the first practice
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        self.heap=[]
        import heapq
        for zero in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap,-zero)
            else:
                if self.heap[0]>-zero:
                    heapq.heapreplace(self.heap,-zero)
                else:
                    continue
    def add(self, val: int) -> int:
        import heapq
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,-val)
        elif -val<self.heap[0]:
            del self.heap[-1]
            heapq.heapify(self.heap)
        heap_f=[-x for x in self.heap]
        return min(heap_f)       

        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# the second practice
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        import heapq
        self.heap=[]
        for i in nums:
            if len(self.heap)<k:
                heapq.heappush(self.heap,i)
            else:
                if self.heap[0]<i:
                    heapq.heapreplace(self.heap,i)
                else:
                    continue

    def add(self, val: int) -> int:
        import heapq
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
        else:
            if self.heap[0]<val:
                heapq.heapreplace(self.heap,val)
        return self.heap[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)