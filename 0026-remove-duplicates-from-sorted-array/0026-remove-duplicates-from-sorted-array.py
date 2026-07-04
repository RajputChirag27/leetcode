class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Let's we have one index keeping track of the element
        # we will check like that first set prev at zero index.
        # and one pointer to track the index.
        # Then we will check if the element change increment the pointer and  # change the prev element 
        n =  len(nums)
        if n <= 1:
            return n
        cIdx = 1
        
        for i in range(1,n):
            if nums[i-1] != nums[i]:
                nums[cIdx] = nums[i]
                cIdx = cIdx + 1
        
        return cIdx