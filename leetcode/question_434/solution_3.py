"""
After reviewing other people's solution, I found out a thought that does not
need to think about the incorrect format that I did for the previous submission.
Loop through the input, loop for the element that is just after the blank space
which is looking for the first element of every segments. However this method
is slower than the second solution I had for some reason.
"""


class Solution:
    def count_segments(self, s: str) -> int:
        prev = " "  # store the previous element in the input
        count = 0  # used to count the number of segments

        for i in s:
            # if the previous element is a space and the current one is not,
            # add count by one
            if i != " " and prev == " ":
                count += 1

            # assign the current element to be the previous element
            # at the end of the for loop
            prev = i

        return count
