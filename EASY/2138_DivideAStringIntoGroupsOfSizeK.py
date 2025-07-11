"""
A string s can be partitioned into groups of size k using the following procedure:

The first group consists of the first k characters of the string, the second group consists of the next k characters of the string, and so on. 
Each element can be a part of exactly one group.
For the last group, if the string does not have k characters remaining, a character fill is used to complete the group.
Note that the partition is done so that after removing the fill character from the last group (if it exists) 
and concatenating all the groups in order, the resultant string should be s.

Given the string s, the size of each group k and the character fill, 
return a string array denoting the composition of every group s has been divided into, using the above procedure.
"""

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        
        cur = ""
        for char in s:
            cur = cur + char
            if len(cur) == k:
                res.append(cur)
                cur = ""
        
        if cur:
            while len(cur) < k:
                cur = cur + fill
            res.append(cur)
        
        return res

"""
this solution is a simple one pass algorithm.
the foundation is simple enough, use a copy variable to house characters until its length meets a certain threshold k.
this repeatedly builds and adds k sized string to our result array.
the added logic comes after the loop finishes and handles our fill.
if cur still exists (is non empty) after the loop finishes, we know we must fill it to size k.
once done we return result.
this solution runs in O(n) linear time.
"""