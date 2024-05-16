class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        >>> Solution().isAnagram("anagram", "nagaram")
        True
        >>> Solution().isAnagram("rat", "car")
        False
        """
        record = [0] * 26
        for i in s:
            record[ord(i) - ord("a")] += 1
        for j in t:
            record[ord(j) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
        return True

    def isAnagram1(self, s: str, t: str) -> bool:
        """
        >>> Solution().isAnagram1("anagram", "nagaram")
        True
        >>> Solution().isAnagram1("rat", "car")
        False
        """
        from collections import Counter

        count_s = Counter(s)
        count_t = Counter(t)
        return count_s == count_t

    def isAnagram2(self, s: str, t: str) -> bool:
        """
        >>> Solution().isAnagram2("anagram", "nagaram")
        True
        >>> Solution().isAnagram2("rat", "car")
        False
        """
        from collections import defaultdict

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in s:
            s_dict[i] += 1
        for j in t:
            t_dict[j] += 1
        return s_dict == t_dict


if __name__ == "__main__":
    import doctest

    doctest.testmod()
