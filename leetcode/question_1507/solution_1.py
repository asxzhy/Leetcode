"""
This solution stores all the month in a list to get its numerical
representation. It uses try except to get the day from the date.
"""


class Solution:
    def reformatDate(self, date: str) -> str:
        # store all the shortcut for the month
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                  'Oct', 'Nov', 'Dec']

        # the month is the last 8 - 6 elements in the input string
        # use the months list to get its numerical representation
        month = months.index(date[-8:-5]) + 1

        # if the month is less than 10, we have to add 0 before the number
        if month < 10:
            month = '0' + str(month)

        # since we don't know if the day is one digit or two digits,
        # we use a try except to get the day from the input string
        try:
            day = int(date[:2])
        except:
            day = int(date[0])

        if day < 10:
            day = '0' + str(day)

        return date[-4:] + "-" + str(month) + "-" + str(day)
