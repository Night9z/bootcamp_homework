class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current_sum = max_sum = nums[0]

        for num in nums[1:]:

            # Otherwise, continue the current subarray
            current_sum = max(num, current_sum + num)
            # Update max sum if current subarray's sum is greater
            max_sum = max(max_sum, current_sum)

        return max_sum