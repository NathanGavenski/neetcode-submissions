class Solution:

    decode_character = "ç"
    def encode(self, strs: List[str]) -> str:
        return ''.join([self.decode_character + s + self.decode_character for s in strs])

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        reading_word = False
        word = ""
        decode_message = []
        for char in s:
            if char == self.decode_character and not reading_word:
                reading_word = True
                continue
            if char == self.decode_character and reading_word:
                reading_word = False
                decode_message.append(word)
                word = ""
                continue
            if reading_word:
                word += char
        return decode_message