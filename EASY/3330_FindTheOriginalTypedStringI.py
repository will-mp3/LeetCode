"""
Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

You are given a string word, which represents the final output displayed on Alice's screen.

Return the total number of possible original strings that Alice might have intended to type.
"""

class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                res += 1
        return res

"""

"""