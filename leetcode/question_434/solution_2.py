"""
Thought: loop through the input, distinguish the segments by looking for blank
spaces. In order to avoid the problem of wrong format such as two blank spaces
between words and having a blank spaces at the end of the input, I added a
boolean variable word_before which is used to determine if the index before the
blank space is not another blank space. This allows me to avoid counting two
number when there is two blank spaces between words. I also checked if the last
element in the input is a space. Only if the last element is not a space, we
need to count one more to include the last word.
"""


class Solution:
    def count_segments(self, s: str) -> int:
        # used to determine if there is word before the blank space
        word_before = False
        # used to count how many segments the variable s has
        count = 0

        for i in s:
            # if there is a blank space at the current index and a word
            # before the space, we add count by one
            if i == " " and word_before:
                count += 1
                word_before = False

            # reset the word_before to True when we pass the blank space
            if i != " " and not word_before:
                word_before = True

        # if the input is not empty and the last element in the input is not
        # a space, we add count by one in order to count on the last word
        if len(s) > 0 and s[-1] != " ":
            count += 1

        return count
