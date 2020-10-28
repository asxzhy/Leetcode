"""
This solution stores the letters and digits to two different lists and add them
into the result list separately
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
        # the result list
        res = []

        # add digits and letters to the corresponding list
        for char in s:
            if char.isdigit():
                numbers.append(char)
            else:
                strings.append(char)

        # add characters into the result list with each type separate apart
        while len(numbers) > 0 or len(strings) > 0:
            # at the first index, check which list has more elements and add
            # the element from the longer list
            if len(res) == 0:
                if diff == 1 or diff == 0:
                    res.append(numbers.pop())
                else:
                    res.append(strings.pop())
            elif res[-1].isdigit():
                # if the previous index contains a digit,
                # add letter to this index
                res.append(strings.pop())
            else:
                # if the previous index contains a letter,
                # add digit to this index
                res.append(numbers.pop())

        return "".join(res)
