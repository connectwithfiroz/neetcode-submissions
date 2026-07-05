class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #AS WE KNOW SET CONTAINS ONLY UNIQUE SO WE CAN COMPARE SET WITH ACTUAL LIST IF BOTH LENTH = HENCE NO DUPLICATE
        return len(set(nums)) != len(nums) # return true if not same (meaning containg duplicate)