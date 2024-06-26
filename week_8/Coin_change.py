class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        # Initialize DP array, with amount+1 (impossible high value) as default
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] <= amount else -1

