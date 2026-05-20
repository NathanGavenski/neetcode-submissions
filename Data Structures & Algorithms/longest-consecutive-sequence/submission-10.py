class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = list(set(nums))
        nums.sort()
        max_count = 0
        count = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1] - 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        return max(max_count, count)
