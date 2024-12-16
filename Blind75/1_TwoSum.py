"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hMap:
                return [hMap[diff], i]
            hMap[n] = i
        return

"""
Create an empty dictionary (hash table). 
find the difference between the target value and the current number in the array. 
Using the array given and the enumerate function iterate through the values and check if the diff variable is in the hash table. 
If it is return, otherwise continue iterating, adding the value and index to the dictionary with each execution.
"""