class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##### min_heap #####
        count_map = Counter(nums)
        min_heap = []

        for num,freq in count_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        
        return[item[1] for item in min_heap]       