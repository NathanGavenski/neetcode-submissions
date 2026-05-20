from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st_anagram = defaultdict(int)
        for x in s:
            st_anagram[x] += 1

        nd_anagram = defaultdict(int)
        for x in t:
            nd_anagram[x] += 1

        return st_anagram == nd_anagram