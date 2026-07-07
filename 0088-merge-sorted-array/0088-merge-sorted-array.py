class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m1 = m - 1
        n1 = n - 1
        mn = m + n - 1

        while m1 >= 0 and n1 >= 0:
            if nums1[m1] >= nums2[n1]:
                nums1[mn] = nums1[m1]
                m1 -= 1
            else:
                nums1[mn] = nums2[n1]
                n1 -= 1
            mn -= 1

        # Running cleanup loop to check it
        while n1 >= 0:
            nums1[mn] = nums2[n1]
            mn -= 1
            n1 -= 1
