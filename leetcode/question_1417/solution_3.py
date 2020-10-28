"""
This solution is pretty similar to the solution two, but this one only iterate
through the shorter list instead of iterating through all the characters
"""


class Solution:
    def reformat(self, s: str) -> str:
        # get the number of digits and characters in the input string
        numbers = sum(num.isdigit() for num in s)
        strings = sum(st.isalpha() for st in s)
        diff = numbers - strings

        # see if the difference is greater than 1
        if diff not in [-1, 0, 1]:
            return ""

        # convert the string into list
        s = [char for char in s]
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

        # separate into three conditions:
        # 1. there are more digits
        # 2. there are more letters
        # 3. there are equal amount of digits and letters
        if len(numbers) > len(strings):
            # if there are more digits, add the digits and letters separately
            # to the result string
            while len(numbers) > 1:
                res += numbers.pop() + strings.pop()

            # add the last digit
            res += numbers.pop()
        elif len(numbers) < len(strings):
            # if there are more letters, add the digits and letters separately
            # to the result string
            while len(strings) > 1:
                res += strings.pop() + numbers.pop()

            # add the last string
            res += strings.pop()
        else:
            # if they are equal amount. There are no extra element we need to
            # consider
            while len(strings) > 0:
                res += strings.pop() + numbers.pop()

        return "".join(res)
