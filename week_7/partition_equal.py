class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If the total sum is odd, it's impossible to split it into two equal parts
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: zero sum is always possible
        
        # Update the dp array
        for num in nums:
            # Traverse backwards to prevent using the same element more than once
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True
        
        return dp[target]

