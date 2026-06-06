class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #------------   (1) ------------ #
        #SHorter but it will traverse entire array even duplicate found so not good
        # seen = set()
        # for num in nums:
        #     if num not in seen:
        #         seen.add(num)
        # return len(seen) != len(nums) #hence some element is duplicate

        #------------   (2 - Optimal)  ------------ #
        #Optimal (stop once duplicate found)
        seen = set[int]()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False #Hence no duplicate found entire array traversed


        