"""
Firstly, I select the shorter string from str1 and str2. Then, I went from the end of the string to use all of it's possible substring to check if it can be repeated to get 
str1 and str2. 
My original method was from the beginning of the shorter string and add the string's letter one by one to a new string. When a letter repeates (exits in the new string), check if 
that new string can be repeated to get those two strings. If not, then keep add letter to the new string. However, I forgot the question is asking for the longest possible 
substring. I was only able to get the shortes substring.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""  # store the out put
        string = ""  # store the shorter string
        # get the shorter string
        if str1 in str2:
            string = str1
        elif str2 in str1:
            string = str2

        if not string: return ""  # if the two strings are not a subset of each other, that means there is not common subtring

        i = len(string)
        while i > 0:
            # check if the subtring can repeat itself to get str1 and str2
            if string[:i] * (len(str1) // len(string[:i])) == str1 and string[:i] * (len(str2) // len(string[:i])) == str2:
                return string[:i]
            i -= 1

        return ""
