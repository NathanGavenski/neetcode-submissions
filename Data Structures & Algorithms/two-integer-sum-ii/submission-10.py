class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_pivot = 0
        r_pivot = len(numbers) - 1
        while l_pivot < r_pivot:
            current = numbers[l_pivot] + numbers[r_pivot]
            if current == target:
                return [l_pivot + 1, r_pivot + 1]
            if current > target:
                r_pivot -= 1
                continue
            if current < target:
                l_pivot += 1
                continue