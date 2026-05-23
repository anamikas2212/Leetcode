#using dictionary to optimise the code to O(n) time complexity
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for current_idx,current_num in enumerate(nums):
            partner_num=target-current_num
            if partner_num in seen:
                partner_idx=seen[partner_num]
                return [current_idx,partner_idx]
            seen[current_num]=current_idx