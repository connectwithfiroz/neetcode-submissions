class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #SHorter but it will traverse entire array even duplicate found so not good
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
        return len(seen) != len(nums) #hence some element is duplicate

        #Optimal (stop once duplicate found)


        