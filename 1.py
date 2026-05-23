class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=len(nums)
        for i in range (0,l):
            for j in range (i+1,l):
                if nums[i]+nums[j]==target :
                    return [i,j]
#has a time complexity of O(n^2) and space complexity of O(1)             

        