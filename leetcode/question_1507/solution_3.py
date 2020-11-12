"""
This solution split the input string into three parts(day, mont, and year).
Then uses a dictionary to get the numerical representation of the month
And checks the length of the day to determine if adding zero is needed
"""


class Solution:
    def reformatDate(self, date: str) -> str:
        # set up a dictionary which corresponds each month to its numerical
        # representation.
        months = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
                  'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
                  'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

        # split the date to [day, month, year]
        date = date.split()
        # if the day is not two digits, return the reformated date
        if len(date[0]) < 4:
            return date[2] + "-" + months[date[1]] + "-" + "0" + date[0][0]

        # if the day is two digits, return the reformated date
        return date[2] + "-" + months[date[1]] + "-" + date[0][0:2]
