class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] > target:
            return 0
        if nums[len(nums)-1] < target:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
 #分类讨论，注意要考虑边界条件
 #https://leetcode.com/problems/search-insert-position/
