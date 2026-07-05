class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #AS WE KNOW SET CONTAINS ONLY UNIQUE SO WE CAN COMPARE SET WITH ACTUAL LIST IF BOTH LENTH = HENCE NO DUPLICATE
        # return len(set(nums)) != len(nums) # return true if not same (meaning containg duplicate)
        
        #approch 2 (using seen )
        seen = set()
        for num in nums:
            # if num in seen hence num is duplicate
            if num in seen:
                return True
            #if number not in seen hence add
            seen.add(num)
        #if not return yet means no dulicate
        return False
