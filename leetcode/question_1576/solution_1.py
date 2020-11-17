"""
This solution changes all of the "?"'s to a character by looping through the
ascii code for lower case characters. If the character is appropriate,
change the "?"
"""


class Solution:
    def modify_string(self, s: str) -> str:
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
                        s = s[:i] + chr(asc)
                        break
                    elif chr(asc) != s[i - 1] and chr(asc) != s[i + 1]:
                        s = s[:i] + chr(asc) + s[i + 1 :]
                        break
                    else:
                        asc += 1

        return s
