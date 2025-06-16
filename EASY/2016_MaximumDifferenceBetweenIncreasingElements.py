"""
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] 
(i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
"""

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l, r = 0, 1
        maxDif = float("-inf")

        while r < len(nums):
            if nums[r - 1] < nums[l]:
                l = r - 1
            maxDif = max(maxDif, nums[r] - nums[l])
            r += 1

        if maxDif <= 0:
            return -1
        
        return maxDif

"""

"""