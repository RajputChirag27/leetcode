class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # twor strings haystack and needle are given
        # I need to return the index of first occurence of needle in haystack,
        # or return -1 if needle is not a part of haystack
        # need to scan the loop two pointers needed and one to keep track of # the start other to scan the word needle if found return index and  # if not found or mismatch the whole word return -1
        # two loops are needed to solve the problem
        # 1 <= haystack.length, needle.length <= 104
        # haystack and needle consist of only lowercase English characters.

        hLen = len(haystack)
        nLen = len(needle)
        tLen = hLen - nLen + 1
        for i in range(tLen):
            match = True
            for j in range(nLen):
                if haystack[i + j] != needle[j]:
                    match = False
                    break

            if match:
                return i

        return -1
