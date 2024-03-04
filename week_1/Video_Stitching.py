from typing import List
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x: x[0])
        count = 0
        currEnd, nextEnd = 0, 0

        for start, end in clips:
            if start > currEnd:
                if start > nextEnd:
                    return -1
                currEnd = nextEnd
                count += 1
            nextEnd = max(nextEnd, end)
            if nextEnd >= time:
                return count + 1

        return -1 if currEnd < time else count

sol = Solution()
print(sol.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10))  
        