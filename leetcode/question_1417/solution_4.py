"""
This solution is similar to solution three but does not use pop() and deleted
the two sum() function at the beginning of the code
"""


class Solution:
    def reformat(self, s: str) -> str:
        # create two lists each only contains digits and letters separately
        numbers = []
        strings = []
        # this variable is used to store the result string
        res = ""

        # add digits and letters to the corresponding list
        for char in s:
            if char.isdigit():
                numbers.append(char)
            else:
                strings.append(char)

        diff = len(numbers) - len(strings)

        if diff not in [-1, 0, 1]:
            return ""

        # separate into three conditions:
        # 1. there are more digits
        # 2. there are more letters
        # 3. there are equal amount of digits and letters
        # but this time iterate through the shorter list
        i = 0
        if len(numbers) > len(strings):
            while i < len(strings):
                res += numbers[i] + strings[i]
                i += 1
            res += numbers[i]
        elif len(numbers) < len(strings):
            while i < len(numbers):
                res += strings[i] + numbers[i]
                i += 1
            res += strings[i]
        else:
            while i < len(strings):
                res += strings[i] + numbers[i]
                i += 1

        return "".join(res)
