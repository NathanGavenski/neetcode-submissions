class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(list(set(nums)))
        max_count = 0
        count = 0
        pivot = nums[0]
        for num in nums[1:]:
            if num == pivot + 1:
                count += 1
            elif num > pivot + 1:
                max_count = max(max_count, count)
                count = 0
            pivot = num
        else:
            max_count = max(max_count, count)
        return max_count + 1
        