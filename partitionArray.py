from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        nums.sort()
        groups = 1            # at least one group
        start = nums[0]       # min of current group

        for x in nums:
            if x - start > k:
                groups += 1
                start = x     # new group's min

        return groups
