class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True

        #     seen.add(num)

        # return False
        #----- #2 Firstly sort array and check if current and previous element are same if yes hence duplicate without extra space
        nums.sort() #sort and update nums list
        for i in range(1 ,len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False
        