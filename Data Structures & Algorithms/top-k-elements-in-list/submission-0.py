class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for n in nums:
            frequency_map[n] = frequency_map.get(n, 0) + 1
        
        #return kth most frequency
        #sort the frequency_map in desc order based on value
        sorted_nums = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)
        #Return the kth position
        return [num for num, _ in sorted_nums[:k]];


        
        