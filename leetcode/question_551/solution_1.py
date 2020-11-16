"""
Use recursive. If there are two A's return will be False. If there are three
continuous L's, return will be False. All other return will be True and they
are connected by and.
"""


class Solution:
    def check_record(self, s: str) -> bool:
        return self.check(s, False)

    def check(self, s, isA):
        # if there is no more letters return true
        if not s:
            return True
        # check if there is three continuous L
        if len(s) > 2 and s[0] == s[1] == s[2] == "L":
            return False

        # check if there is two A
        if isA and s[0] == "A":
            return False

        # if there is one A, change the variable isA
        if s[0] == "A":
            isA = True

        return True and self.check(s[1:], isA)
