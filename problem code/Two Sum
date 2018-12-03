class Solution:
    def twoSum(self, nums, target):
        store = dict()
        for i in range(len(nums)):
            search = target - nums[i]
            if search in store:
                return [store[search],i]
            else:
                store[nums[i]] = i
        return 0
        
