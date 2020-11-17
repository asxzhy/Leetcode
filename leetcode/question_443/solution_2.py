"""
This solution loops through the list, record the last character before a new
character to calculate the total amount of a character. Use a count to keep
track of which index we need to put the character and its length in.
"""


class Solution:
    def compress(self, chars) -> int:
        index_prev = -1  # store the previous character's index
        count = -1  # count the number of elements that are changed

        for i in range(0, len(chars)):
            # if the character will change at the next index or it is the
            # last element in the list
            if i == len(chars) - 1 or chars[i] != chars[i + 1]:
                if index_prev + 1 == i:  # check if the character is by itself
                    count += 1
                    # replace the element at the front of the list to be this
                    # character
                    chars[count] = chars[i]
                else:
                    # if the character is not by itself, then we need to add
                    # its total amount
                    count += 2
                    chars[count - 1] = chars[i]

                    # if the total amount if greater than 9 smaller than 100,
                    # we need two spaces for it
                    if i - index_prev > 9:
                        count += 1
                        chars[count - 1] = str((i - index_prev) // 10)
                        chars[count] = str((i - index_prev) % 10)
                    else:
                        chars[count] = str(i - index_prev)

                index_prev = i

        return count + 1
