class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]  # Initialize current sum with the first element
        max_sum = nums[0]  # Initialize max sum with the first element
        
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])  
            max_sum = max(max_sum, current_sum)  
        
        return max_sum
