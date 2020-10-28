"""
If the difference in the number of digits and characters is greater than one,
then it is not possible to create a string that can separate the characters
and strings.
To create a string that doesn't have two adjacent characters have the same type
I iterated through the list and moved the every character to the end of the
list whenever there are two adjacent characters have the same type
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
        res = [char for char in s]
        index = 1

        # if there are more digits in the string or there are equal amount of
        # characters and digits in the string
        # put a digit to the front of the list
        if diff == 1 or diff == 0:
            for i in range(0, len(res)):
                if res[i].isdigit():
                    res.insert(0, res.pop(i))
                    break

        # if there are more character in the string
        # put a character to the front of the list
        if diff == -1:
            for i in range(0, len(res)):
                if res[i].isalpha():
                    res.insert(0, res.pop(i))
                    break

        # if the previous index and current index have the same type of value
        # stored (ig. char and char / digit and digit)
        # then move the value at the current index to the end of the list
        while index < len(res):
            if (res[index - 1].isalpha() and res[index].isalpha()) or (
                res[index - 1].isdigit() and res[index].isdigit()
            ):
                res.append(res.pop(index))
            else:
                index += 1

        return "".join(res)
