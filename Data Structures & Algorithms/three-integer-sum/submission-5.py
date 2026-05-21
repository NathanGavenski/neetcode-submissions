from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for pivot, a in enumerate(nums):
            if pivot > 0 and a == nums[pivot - 1]:
                continue
    
            left, right = pivot + 1, len(nums) - 1
            while left < right:
                current = a + nums[left] + nums[right]
                if current > 0:
                    right -= 1
                elif current < 0:
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result