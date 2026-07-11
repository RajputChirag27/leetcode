class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        Problem: 594. Longest Harmonious Subsequence
        
        Key Insight: 
        - Subsequences do NOT need to be contiguous. 
        - A harmonious subsequence can only contain two distinct numbers: x and x + 1.
        - Therefore, the max length for a pair is simply: count(x) + count(x + 1).

        Strategy:
        1. Build a frequency map of all elements in `nums`.
        2. Iterate through the unique keys in the map.
        3. If `key + 1` exists, calculate the combined frequency and track the maximum.

        Complexity Goals:
        - Time: O(n) - Single pass to count, single pass to check pairs.
        - Space: O(n) - To store element frequencies in the hash map.
        """
        # Your code goes here

        freqMap = Counter(nums)
        maxSum = 0

        for i in range(len(nums)):
            if nums[i]+1 in freqMap:
                maxSum = max(maxSum, freqMap.get(nums[i])+ freqMap.get(nums[i]+1))
            
        return maxSum
