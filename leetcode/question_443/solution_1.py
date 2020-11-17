"""
This solution is pretty messy
"""


class Solution:
    def compress(self, chars) -> int:
        count = -1  # count how many characters are in the chars
        idx_prev = 0

        for i in range(0, len(chars) - 1):
            # if the current character is not the same as the next character
            if chars[i] != chars[i + 1]:
                if i == 0:
                    # if the change occurs at index 0, that means there is only
                    # first character is unique, nothing need to be replaced
                    count += 1
                elif chars[i - 1] != chars[i]:
                    # if the character is unique
                    count, chars = self.replaceChar(
                        count,
                        chars,
                        True,
                        i,
                        idx_prev,
                    )
                else:
                    # add count by two, move the character to the front and let
                    # the next element be the total number of the same character
                    count, chars = self.replaceChar(
                        count,
                        chars,
                        False,
                        i,
                        idx_prev,
                    )
                idx_prev = i + 1

        # if the length of the chars is one, just add
        # count by one. Other needs to be replaced
        if len(chars) == 1:
            count += 1
        elif len(chars) != 0:
            # used to deal with the character at the end of the list
            if chars[-2] != chars[-1]:
                # if the character is unique
                count, chars = self.replaceChar(
                    count,
                    chars,
                    True,
                    len(chars) - 1,
                    idx_prev,
                )
            else:
                count, chars = self.replaceChar(
                    count,
                    chars,
                    False,
                    len(chars) - 1,
                    idx_prev,
                )

        return count + 1

    def replace_char(self, count, chars, is_unique, i, idx_prev):
        # used to put the current character and its total amount to the front
        if is_unique:
            count += 1
            chars[count] = chars[i]
        else:
            total = i - chars.index(chars[i], idx_prev) + 1
            if total >= 10:
                count += 3
                chars[count - 2] = chars[i]
                chars[count - 1] = str(total // 10)
                chars[count] = str(total % 10)
            else:
                count += 2
                chars[count - 1] = chars[i]
                chars[count] = str(total)

        return count, chars
