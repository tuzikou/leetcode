class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        rtype = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[rtype] = nums[i]
                rtype += 1
        return rtype
