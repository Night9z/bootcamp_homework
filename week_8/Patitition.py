class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True  
        
        # Update the dp array
        for num in nums:

            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True
        
        return dp[target]
