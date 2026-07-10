class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # =========================================================================
        # LEETCODE 209: Minimum Size Subarray Sum (Medium)
        # Pattern: Variable-Size Sliding Window (Shortest Valid Window)
        # Time Complexity Goal: O(n) - Single pass with two pointers
        # Space Complexity Goal: O(1) - In-place tracking variables
        # =========================================================================
        # INPUT:
        #   - target: int (Value we must meet or exceed)
        #   - nums: List[int] (Array of POSITIVE integers)
        #
        # RETURN:
        #   - int (Minimal window length, or 0 if impossible)
        #
        # STRATEGY & BOUNDARIES:
        #   - Use two pointers: 'i' (left) and 'j' (right) starting at 0.
        #   - Initialize 'min_len' to len(nums) + 1 to track the "not found" state.
        #   - Expand 'j' to absorb elements into a running sum.
        #   - Use a 'while' loop to shrink 'i' as long as running_sum >= target.
        #   - Inside the shrink loop, record the minimal window size: j - i + 1.
        # =========================================================================

        n = len(nums)
        minLen = n + 1
        currSum = 0
        i = 0

        for j in range(n):
            currSum += nums[j]

            while currSum >= target:
                minLen = min(minLen, j - i + 1)
                currSum -= nums[i]
                i += 1

        if minLen == n + 1:
            return 0
        return minLen
