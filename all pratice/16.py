class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_sorted=sorted(nums,reverse=True)
        return nums_sorted[k-1]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap=[]
        for i in range(k):
            x=nums.pop()
            heapq.heappush(heap,x)
        while nums:
            x=nums.pop()
            if x>heap[0]:
                heapq.heapreplace(heap,x)
            else:
                continue
        return heap[0]