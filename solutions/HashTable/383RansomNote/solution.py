class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        >>> s = Solution()
        >>> s.canConstruct("a", "b")
        False
        >>> s.canConstruct("aa", "ab")
        False
        >>> s.canConstruct("aa", "aab")
        True
        """
        # from collections import Counter
        # return not Counter(ransomNote) - Counter(magazine)
        counts = {}
        for c in magazine:
            counts[c] = counts.get(c, 0) + 1
        for c in ransomNote:
            if c not in counts or counts[c] == 0:
                return False
            counts[c] -= 1
        return True