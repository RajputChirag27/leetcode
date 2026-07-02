class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        goodIdx = 0
        n = len(nums)
        for i in range(n):
            if(nums[i] != val):
                nums[goodIdx] = nums[i]
                goodIdx = goodIdx + 1
            
        return goodIdx