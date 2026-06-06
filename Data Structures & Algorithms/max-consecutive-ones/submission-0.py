class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_1s = 0;
        latest_count = 0
        for i in nums:
            if i==1:
                latest_count = latest_count+1
                if latest_count > max_1s:
                    max_1s = latest_count
            else:
                latest_count = 0
        return max_1s
        