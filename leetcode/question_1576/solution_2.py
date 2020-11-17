"""
This solution is similar to the solution 1. It uses a list instead of adding
all the characters up to get a string whenever it changes the "?" sign.
This solution simple changes the "?" sign at its index
"""


class Solution:
    def modify_string(self, s: str) -> str:
        # split every characters in the input string
        s = list(s)

        # check every character in the input string.
        # if it is a "?", do the some method to accomplish the goal
        for i in range(len(s)):
            if s[i] == "?":

                # loop through ascii code from 97 to 122
                # change the "?" to a character that is not the same as the
                # characters at the previous index and the next index
                asc = 97
                while asc < 123:
                    if i == len(s) - 1 and chr(asc) != s[i - 1]:
                        s[i] = chr(asc)
                        break
                    elif chr(asc) != s[i - 1] and chr(asc) != s[i + 1]:
                        s[i] = chr(asc)
                        break
                    else:
                        asc += 1

        return "".join(s)
