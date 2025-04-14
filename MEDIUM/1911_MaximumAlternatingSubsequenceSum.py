"""
The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of the elements at odd indices.

For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
Given an array nums, return the maximum alternating sum of any subsequence of nums (after reindexing the elements of the subsequence).

A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) 
without changing the remaining elements' relative order. 
For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.
"""

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # sumAdd -> first value in subsequence was added
        # sumSubtract -> first value in subsequence was subtracted
        sumAdd, sumSubtract = 0, 0 # current maxes

        for i in range(len(nums) - 1, -1, -1):
            # compute maximum if we are adding
            tmpAdd = max(sumSubtract + nums[i], sumAdd)

            # compute maximum if we are subtracting
            tmpSubtract = max(sumAdd - nums[i], sumSubtract)

            sumAdd, sumSubtract = tmpAdd, tmpSubtract # new maxes

        return max(sumAdd, sumSubtract)

"""

"""