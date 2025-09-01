class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        res = []
        for i in nums:
            dic[i] = 1+ dic.get(i,0)
        
        heap = [[-occur,value] for value,occur in dic.items()]
        
        heapq.heapify(heap)
        
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
