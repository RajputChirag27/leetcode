class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        # =========================================================================
        # LEETCODE 3: Longest Substring Without Repeating Characters (Medium)
        # Pattern: Variable-Size Sliding Window (Longest Valid Window)
        # Time Complexity Goal: O(n) - Linear scan using a sliding accordion
        # Space Complexity Goal: O(min(m, n)) - Set storing unique characters
        # =========================================================================
        # INPUT:
        #   - s: str (The input string consisting of letters, digits, symbols)
        #
        # RETURN:
        #   - int (Length of the longest substring with NO repeating characters)
        #
        # STRATEGY & ORDER OF OPERATIONS:
        #   - Use two pointers: 'i' (left) and 'j' (right) starting at 0.
        #   - Maintain a Python set() named 'char_set' to track window elements.
        #   - Loop 'j' through the string:
        #       1. SHRINK PHASE: If s[j] is in char_set, while loop removes s[i]
        #          from the set and increments 'i' until s[j] is no longer a duplicate.
        #       2. EXPAND PHASE: Add the current valid character s[j] to char_set.
        #       3. CAPTURE PHASE: Update max_len using max(max_len, j - i + 1).
        # =========================================================================

        """

        n = len(s)
        maxLen = 0
        i = 0
        charSet = set()

        for j in range(n):
            # if s[j] in charSet:
            while s[j] in charSet:
                charSet.remove(s[i])
                i = i + 1
            
            charSet.add(s[j])
            maxLen = max(maxLen, j - i + 1)

        return maxLen
