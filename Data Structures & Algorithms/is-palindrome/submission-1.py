class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = re.compile('[^a-zA-Z0-9]')
        clean_string = pattern.sub('', s).lower()
        return clean_string == clean_string[::-1]
        