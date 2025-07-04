"""
You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:

Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
Return the lexicographically smallest resulting string after removing all '*' characters.
"""

class MySolution:
    def clearStars(self, s: str) -> str:
        
        nStr = []
        cnt = [ 0 for _ in range(26) ] # [character index, count]

        def remove_min(string):
            # find min char using index based count array
            for i in range(26):
                if cnt[i]:
                    min = chr(ord('a') + i) # decode indexes 0 - 25 using unicode equivalent
                    cnt[i] -= 1
                    break

            # traverse new string backwards, removing first instance of min char
            for i in range(len(string) - 1, -1, -1):
                if string[i] == min:
                    del string[i]
                    return

        for i, char in enumerate(s):

            # if star is found, call helper function on current string built
            if char == "*":
                remove_min(nStr)
                continue

            # if not a star: add char to new string, get character index based on unicode value, increment count of said index
            nStr.append(char)
            charIdx = ord(char) - ord('a')
            cnt[charIdx] += 1

        return ''.join(nStr)
    
class OptimalSolution:
    def clearStars(self, s: str) -> str:
        cnt = [[] for _ in range(26)]
        arr = list(s)
        for i, c in enumerate(arr):
            if c != "*":
                cnt[ord(c) - ord("a")].append(i)
            else:
                for j in range(26):
                    if cnt[j]:
                        arr[cnt[j].pop()] = "*"
                        break
        return "".join(c for c in arr if c != "*")

"""
ive included two solution for this problem with similar logic.
one of them is my own which failed one text case but is easier to understand and the other is the optimal solution.
the simple logic of this problem is that we have to traverse our string until we find an asterisk.
once found, we remove the nearest, smallest character in the left partition from the found asterisk.
we do this by tracking our characters seen and their counts in a count array.
we use unicode values for our characters where the index matches the specific character.
each time one is seen we increment its index.
if an asterisk is found we call a helper function which finds the smallest character with a count and searches our new string for it.
we search backwards from the asterisk to find the first one available to keep the string as lexicographically small as possible.
"""