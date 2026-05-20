class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "<EMPTY>"
        return "<TOKEN>".join(strs)

    def decode(self, s: str) -> List[str]:
        if "<EMPTY>" in s:
            return []
        return s.split("<TOKEN>")