class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # NOT OPTIMAL
        # for i, num in enumerate(nums):
        #     target2 = target - num
        #     for j, num2 in enumerate(nums):
        #         if i==j:
        #             continue;
        #         else:
        #             if num2 == target2:
        #                 return [i, j]
        # return [0,0]
        #2. NOt optimal
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        #OPTIMAL - Using hashmap
        seen = {}
        
        # for i, num in enumerate(nums):
        #     complement = target - num;
        #     if complement in seen:
        #         return [seen(complement), i]
        #     #else add in hashmap num => index
        #     seen[num] = i;
        


        