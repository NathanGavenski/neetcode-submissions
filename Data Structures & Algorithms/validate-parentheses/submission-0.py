class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(", "{", "["]
        closing = [")", "}", "]"]
        stack = []
        for char in s:
            if char in opening:
                stack.append(char)
            if char in closing:
                if len(stack) == 0:
                    return False

                pair = stack.pop()
                if opening.index(pair) != closing.index(char):
                    return False

        return len(stack) == 0