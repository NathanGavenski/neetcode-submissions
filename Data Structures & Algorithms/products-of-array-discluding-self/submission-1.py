class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        product = [1] * size
        for i in range(size):
            for j in range(size):
                if i != j:
                    product[i] *= nums[j]
        return product
        