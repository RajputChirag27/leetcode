class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # nums is given consisting of n elements (len(nums)) and an integer k
        # yeah so our window is k
        # Any answer with a calculation error less than 10^-5 will be accepted
        # Constraints are 10^5 O(n) will be accepted here
        # nums[i] can be negative

        currSum = sum(nums[:k])
        maxSum = currSum
        n = len(nums)

        for i in range(k, n):
            currSum = currSum + nums[i] - nums[i - k]
            maxSum = max(maxSum, currSum)

        result = maxSum / k
        return result
