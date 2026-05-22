class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i, today in enumerate(temperatures):
            count = 1
            for j, next_days in enumerate(temperatures[i+1:]):
                if next_days > today:
                    result.append(count)
                    break
                count += 1
            else:
                result.append(0)
        return result