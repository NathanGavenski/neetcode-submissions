from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        return max(count.values()) > 1