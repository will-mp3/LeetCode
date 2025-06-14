"""
You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

Notes:

When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
Bob can remap a digit to itself, in which case num does not change.
Bob can remap different digits for obtaining minimum and maximum values respectively.
The resulting number after remapping can contain leading zeroes.
"""

class Solution:
    def minMaxDifference(self, num: int) -> int:
        minS, maxS = str(num), str(num)

        # find digit to replace for max
        for x in maxS:
            if x != "9":
                maxRep = x
                break
            maxRep = "9"

        minS = minS.replace(maxS[0], "0")
        maxS = maxS.replace(maxRep, "9")

        return int(maxS) - int(minS)

"""

"""