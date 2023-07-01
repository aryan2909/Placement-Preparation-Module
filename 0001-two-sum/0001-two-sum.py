class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        num_dict = {} 
        
        for i in range(n):
            complement = target - nums[i]
            
            if complement in num_dict:
                return [num_dict[complement], i]
            
            num_dict[nums[i]] = i
        
        return "No solution found."
