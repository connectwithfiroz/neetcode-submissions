class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #in this question we need to return indexed so never sort list 
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [0, 0]

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # we can substract first element from target  and check is exist in remaining list if yes then return index of that element
        # i = 0
        # for i in range(len(nums)-1):
        #     search_target = target - nums[i]
        #     if search_target in nums[i+1:]:
        #         return [i, nums.index(search_target)]
            


        #APPROACH - 2 (BY USING TWO POINTER LAST AND FIRST FROM FIRS AND LAST MOVE CURSOR)
        # Only work if array contain non negative number and in increaseing order 
        # i = 0
        # j = len(nums) - 1

        # while (i < j):
        #     sum_of_ij = nums[i] + nums[j]
        #     if sum_of_ij == target:
        #         return [i, j]
        #     elif sum_of_ij > target:
        #         j -= 1
        #     elif sum_of_ij < target:
        #         i += 1

        # return [i, j]
            
