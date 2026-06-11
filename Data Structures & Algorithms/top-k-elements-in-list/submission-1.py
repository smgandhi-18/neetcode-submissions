class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##### bucket sort approach
        buckets = [ [] for _ in range(len(nums) + 1)]
        count_map = Counter(nums)

        for num,freq in count_map.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if(len(result)==k):
                    return result
                         