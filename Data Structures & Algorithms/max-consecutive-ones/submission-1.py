class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_1s = 0;
        latest_count = 0
        for num in nums:
            if num==1:
                latest_count = latest_count+1
                max_1s = max(max_1s, latest_count)
                # if latest_count > max_1s:
                #     max_1s = latest_count
            else:
                latest_count = 0
        return max_1s
        