class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_count = 0
        max_length = 0
        start = 0

        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            max_count = max(max_count, count[s[end]])

            while (end - start + 1) - max_count > k:
                count[s[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)
        return max_length

