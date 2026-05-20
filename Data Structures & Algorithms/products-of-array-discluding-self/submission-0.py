from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        stack = []
        for i in range(len(nums)):
            _nums = nums[:i] + nums[i+1:]
            stack.append(prod(_nums))
        return stack