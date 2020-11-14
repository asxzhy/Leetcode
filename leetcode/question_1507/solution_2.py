"""
This solution used the same concept as solution 1 to solve the question but
used if statement instead of try except.
"""


class Solution:
    def reformatDate(self, date: str) -> str:
        # store all the shortcuts for the months
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                  'Oct', 'Nov', 'Dec']

        # the month is the last 8 - 6 elements in the input string
        # use the months list to get its numerical representation
        month = months.index(date[-8:-5]) + 1
        if month < 10:
            month = '0' + str(month)

        # instead of using a try except, we check if the day is two digits
        if date[:2].isdigit():
            day = date[:2]
        else:
            day = '0' + date[0]

        return date[-4:] + "-" + str(month) + "-" + str(day)
