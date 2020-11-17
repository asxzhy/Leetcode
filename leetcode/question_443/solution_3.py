class Solution:
    def compress(self, chars) -> int:
        index = 0  # keep track of the index
        count = 0  # keep track of the index that is being replaced

        while index < len(chars):
            char = chars[index]  # store the first character
            freq = 0  # reset the frequency to zero

            # if the character is still same as the stored first character,
            # then add frequency by one and go to the next index
            while index < len(chars) and char == chars[index]:
                index += 1
                freq += 1

            # replace element at the front to be the character that has been
            # checked
            chars[count] = char
            count += 1

            # if the amount of character is greater than one, then add the
            # amount behind the character
            if freq > 1:
                # if the number is greater than 9, we need two or more spaces
                # to add the number
                for i in str(freq):
                    chars[count] = i
                    count += 1

        return count
