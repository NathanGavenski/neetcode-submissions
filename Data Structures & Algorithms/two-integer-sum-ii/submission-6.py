class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_pivot = 0
        r_pivot = len(numbers) - 1
        while True:
            if numbers[l_pivot] + numbers[r_pivot] > target:
                r_pivot -= 1
                continue
            if numbers[l_pivot] + numbers[r_pivot] < target:
                l_pivot += 1
                continue
            if numbers[l_pivot] + numbers[r_pivot] == target:
                return [l_pivot + 1, r_pivot + 1]